from abc import ABC, abstractmethod
from typing import List

from .status import Paper


class PrinterCoreABC(ABC):
    @abstractmethod
    def _stread(self, buf) -> str:
        pass

    @abstractmethod
    def raw_decimal(self, msg):
        pass

    @abstractmethod
    def expand_bit_by_bit(self, byte, hash) -> List:
        pass

    @abstractmethod
    def init(self):
        """
        Initialize printer($1B $40)
            [Description] Clears the data in the print buffer and resets the printer mode to that in effect when power was
                            turned on.
            [Notes] • The data in the receiver buffer is not cleared.
                    • The macro defi nitions are not cleared.
        """
        pass

    @abstractmethod
    def present(self, steps: int = 2, blink: bool = True, out: str = 'R', out_delay=10):
        """
        Present command ($1C $50)
            This command cuts the paper and present/retract the ticket.
                • 'steps' indicates the number of steps for the ticket present (1 step = 5mm)
                • 'blink' indicates the behaviour of the paper mouth as follow:
                       b FUNCTION
                       0 Paper mouth: led OFF
                       1 Paper mouth: led blinking
                • 'out' indicates the ticket movement after the print as follow:
                       'E' Eject ticket
                       'R' Retract ticket
                • 'out_delay' indicates the timeout for the ticket present (1 = 1 second)
        """
        pass

    @abstractmethod
    def retract(self):
        """ Retract command"""
        pass

    @abstractmethod
    def paper_status(self) -> Paper:
        pass


class PrinterABC(PrinterCoreABC, ABC):
    @abstractmethod
    def print(self, text, present_command):
        pass

    @abstractmethod
    def save_paper_state(self):
        pass

    @abstractmethod
    def isTakeCheque(self, time_: int) -> bool:
        pass

    @abstractmethod
    def waitTicketState(self, state, time_perf) -> bool:
        pass
