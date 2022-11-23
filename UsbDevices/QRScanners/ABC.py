from abc import ABC, abstractmethod


class TypeConnect:
    HID = 'hid'
    COM_PORT = 'com_port'


class QRScannerABC(ABC):
    @abstractmethod
    def read(self, *args, **kwargs) -> bytes:
        pass

    def is_open(self) -> bool:
        pass
