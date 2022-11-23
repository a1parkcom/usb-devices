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

    def read(self, size=128) -> bytes:
        return self.ser.readline(size)

    def is_open(self) -> bool:
        return self.ser.is_open


class Scanner(Thread):
    def __init__(self, scanner: QRScannerABC, func=None):
        super(Scanner, self).__init__()
        self.scanner = scanner
        self.qr_code = None
        self.func = func if func is not None else lambda e: None

    def run(self):
        while self.is_alive():
            self.qr_code = self.scanner.read()
            if self.qr_code is not None:
                self.func(self.qr_code)
                self.qr_code = None
                time.sleep(2)
            time.sleep(0.05)

    def code(self) -> bytes:
        return self.qr_code
