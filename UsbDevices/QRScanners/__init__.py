import time
from typing import TextIO
from threading import Thread

import evdev
import serial
from evdev import InputDevice, categorize, ecodes


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
        data = self.ser.readline(size).decode('utf-8').strip()
        if data:
            return data[data[0] != 'h'::]
        return ''

    def is_open(self) -> bool:
        return self.ser.is_open

    def open(self):
        self.ser.open()

    def close(self):
        self.ser.close()


class HIDPOSBase(QRScannerABC):
    def __init__(self, file_path: str='/dev/hidraw0'):
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

    def open(self) -> InputDevice:
        self.dev = InputDevice(self.event_path)
        self.dev.grab()
        return self.dev

    def close(self):
        self.dev.close()
        self.dev = None

    def is_open(self) -> bool:
        return self.dev is not None


class TestScanner(QRScannerABC):
    def __init__(self, file_path: str='scannerdata'):
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
    def __init__(self, scanner: QRScannerABC, func=None):
        super(Scanner, self).__init__()
        self.scanner = scanner
        self.qr_code = ''
        self.func = func
        self.start()

    def run(self):
        while self.is_alive() and self.scanner.is_open():
            self.qr_code = self.scanner.read()
            if self.qr_code:
                if callable(self.func):
                    print(self.qr_code)
                    self.func(self.qr_code)

        self.scanner.close()

        print('Scanner connection closed, thread stopped')

    def code(self) -> str:
        return self.qr_code


if __name__ == '__main__':
    sc = HIDPOSBase('/dev/hidraw1')
    print(sc.read())