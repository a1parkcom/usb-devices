import logging
from threading import Thread
from typing import TextIO

import aioserial
import serial
from websockets.sync.client import connect, ClientConnection

from .ABC import QRScannerABC, TypeConnect
from .encodings import Mindeo


class SerialBase(QRScannerABC):
    def __init__(self, port: str, baudrate=9600, timeout=0):
        self.ser = serial.Serial(port,
                                 baudrate=baudrate,
                                 parity=serial.PARITY_NONE,
                                 stopbits=serial.STOPBITS_ONE,
                                 bytesize=serial.EIGHTBITS,
                                 timeout=timeout)

    def read(self, size=None) -> str:
        try:
            data = self.ser.readline(size).decode('utf-8').strip()
            if data:
                return data[data[0] != 'h'::]
        except:
            pass
        return ''

    def is_open(self) -> bool:
        return self.ser.is_open

    def open(self):
        self.ser.open()

    def close(self):
        self.ser.close()


class AIOSerialBase(QRScannerABC):
    def __init__(self, port: str, baudrate=9600, timeout=0):
        self.ser = aioserial.AioSerial(port,
                                       baudrate=baudrate,
                                       parity=serial.PARITY_NONE,
                                       stopbits=serial.STOPBITS_ONE,
                                       bytesize=serial.EIGHTBITS,
                                       timeout=timeout)

    async def read(self, size=None) -> str:
        try:
            data = (await self.ser.readline_async(size)).decode(errors='ignore').strip()
            if data:
                return data[data[0] != 'h'::]
        except:
            pass
        return ''

    def is_open(self) -> bool:
        return self.ser.is_open

    def open(self):
        self.ser.open()

    def close(self):
        self.ser.close()


class HIDPOSBase(QRScannerABC):
    def __init__(self, file_path: str = '/dev/hidraw0'):
        self.file_path = file_path

        self.f: TextIO = self.open()

    def read(self, size=None) -> str:
        data = self.f.readline()
        return data

    def is_open(self) -> bool:
        return bool(self.f)

    def open(self) -> TextIO:
        return open(self.file_path, 'r')

    def close(self):
        if self.is_open():
            self.f.close()


class HIDPOSEventBase(QRScannerABC):

    def __init__(self, event_path='/dev/input/event7'):
        try:
            import evdev
            from evdev import InputDevice, categorize, ecodes
        except ModuleNotFoundError as e:
            logging.critical('Please install evdev module')
            exit()

        self.event_path = event_path
        self.dev = self.open()

    def read(self, *args, **kwargs) -> str:
        x = ''
        caps = False

        for event in self.dev.read_loop():
            if event.type == ecodes.EV_KEY:
                data = categorize(event)

                if data.scancode == 42:
                    caps = bool(data.keystate)

                elif data.scancode == 28:
                    return x

                elif data.keystate == 1:
                    x += '{}'.format(Mindeo().get(caps, data.scancode))

    def open(self):
        self.dev = InputDevice(self.event_path)
        self.dev.grab()
        return self.dev

    def close(self):
        self.dev.close()
        self.dev = None

    def is_open(self) -> bool:
        return self.dev is not None


class TestScanner(QRScannerABC):
    def __init__(self, file_path: str = 'scannerdata'):
        self.file_path = file_path

        self.f: TextIO = self.open()

    def read(self, size=None) -> str:
        return self.f.readline()

    def is_open(self) -> bool:
        return bool(self.f)

    def open(self) -> TextIO:
        return open(self.file_path, 'r')

    def close(self):
        if self.is_open():
            self.f.close()


class Scanner(Thread):
    def __init__(self, scanner: QRScannerABC, func=None, size=None):
        super(Scanner, self).__init__()
        self.scanner = scanner
        self.qr_code = ''
        self.func = func
        self.size = size
        self.start()

    def run(self):
        while self.is_alive() and self.scanner.is_open():
            self.qr_code = self.scanner.read(self.size)
            if isinstance(self.qr_code, str) and self.qr_code:
                if callable(self.func):
                    self.func(self.qr_code)

        self.scanner.close()

        print('Scanner connection closed, thread stopped')

    def code(self) -> str:
        return self.qr_code


class AsyncScanner(Thread):
    def __init__(self, scanner: AIOSerialBase, func=None, size=None):
        super(AsyncScanner, self).__init__()
        self.scanner = scanner
        self.qr_code = ''
        self.func = func
        self.is_alive = True
        self.size = size

    async def run(self):
        while self.scanner.is_open() and self.is_alive:
            self.qr_code = await self.scanner.read(self.size)
            if isinstance(self.qr_code, str) and self.qr_code:
                await self.func(self.qr_code)

    def stop(self):
        self.is_alive = False

    def code(self) -> str:
        return self.qr_code


class WebSocketScanner(QRScannerABC):
    def __init__(self, addr, additional_headers: dict = None):
        self.addr = addr
        self.additional_headers = additional_headers

        self._is_open = False
        self._connect: ClientConnection = None
        self.open()

    def open(self):
        self.close()
        self._connect = connect(self.addr, additional_headers=self.additional_headers)
        self._is_open = True

    def close(self):
        if self._connect is not None:
            self._connect.close()
        self._is_open = False

    def is_open(self) -> bool:
        return self._is_open

    def read(self, *args, **kwargs) -> str:
        if not self.is_open():
            return ""
        try:
            data = self._connect.recv()
            return f"{data}"
        except TimeoutError:
            return ""


if __name__ == '__main__':
    sc = WebSocketScanner('ws://89.17.56.214:7878/scanner/ws')
    print(sc.read())
