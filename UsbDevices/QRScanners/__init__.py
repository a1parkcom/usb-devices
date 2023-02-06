import time
from typing import TextIO

import serial

from .ABC import QRScannerABC, TypeConnect
from threading import Thread
from io import TextIOBase


class SerialScanner(QRScannerABC):
    def __init__(self, port: str, baudrate=9600, timeout=0):
        self.ser = serial.Serial(port,
                                 baudrate=baudrate,
                                 parity=serial.PARITY_NONE,
                                 stopbits=serial.STOPBITS_ONE,
                                 bytesize=serial.EIGHTBITS,
                                 timeout=timeout)

    def read(self, size=None) -> str:
        return self.ser.readline(size).decode('utf-8')

    def is_open(self) -> bool:
        return self.ser.is_open

    def open(self):
        self.ser.open()

    def close(self):
        self.ser.close()


class HIDPOSScanner(QRScannerABC):
    def __init__(self, file_path: str='/dev/hidraw0'):
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
                    self.func(self.qr_code)
                    time.sleep(2)

        self.scanner.close()

        print('Scanner connection closed, thread stopped')

    def code(self) -> str:
        return self.qr_code


if __name__ == '__main__':
    sc = HIDPOSScanner('/dev/hidraw1')
    print(sc.read())