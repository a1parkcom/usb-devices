import time

import serial

from .ABC import QRScannerABC, TypeConnect
from threading import Thread


class SerialScanner(QRScannerABC):
    def __init__(self, port: str, baudrate=9600, timeout=0):
        self.ser = serial.Serial(port,
                                 baudrate=baudrate,
                                 parity=serial.PARITY_NONE,
                                 stopbits=serial.STOPBITS_ONE,
                                 bytesize=serial.EIGHTBITS,
                                 timeout=timeout)

    def read(self, size=None) -> bytes:
        return self.ser.readline(size)

    def is_open(self) -> bool:
        return self.ser.is_open

    def open(self):
        self.ser.open()

    def close(self):
        self.ser.close()


class Scanner(Thread):
    def __init__(self, scanner: QRScannerABC, func=None):
        super(Scanner, self).__init__()
        self.scanner = scanner
        self.qr_code = b''
        self.func = func if func is not None else lambda e: None

    def run(self):
        while self.is_alive() and self.scanner.is_open():
            self.qr_code = self.scanner.read()

            if self.qr_code:
                self.func(self.qr_code)
                time.sleep(2)
            time.sleep(0.05)

            self.qr_code = b''
        self.scanner.close()

        print('Scanner connection closed, thread stopped')

    def code(self) -> bytes:
        return self.qr_code
