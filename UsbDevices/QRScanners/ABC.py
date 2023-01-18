from abc import ABC, abstractmethod


class TypeConnect:
    HID = 'hid'
    COM_PORT = 'com_port'


class QRScannerABC(ABC):
    @abstractmethod
    def read(self, *args, **kwargs) -> str:
        pass

    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def close(self):
        pass

    @abstractmethod
    def is_open(self) -> bool:
        pass
