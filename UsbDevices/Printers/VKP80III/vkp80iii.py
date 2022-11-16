import logging

from escpos.exceptions import USBNotFoundError
from escpos.printer import Usb
from logdecorator import log_on_end, log_on_error
from usb.core import NoBackendError

from .constants import PAPER_STATUS_VKP80III
from ..Core.status import Paper
from ..Core.utils import dec_to_hex


class VKP80III(Usb):
    @log_on_error(logging.CRITICAL, "Принтер не найден!!!"
                                    "(idVendor={idVendor}, idProduct={idProduct}, in_ep={in_ep}, out_ep={out_ep})",
                  on_exceptions=(USBNotFoundError, NoBackendError),
                  reraise=False)
    def __init__(self, idVendor=0x0dd4, idProduct=0x0205, timeout=0, in_ep=0x81, out_ep=0x02, *args, **kwargs):
        super(VKP80III, self).__init__(idVendor, idProduct, timeout, in_ep, out_ep, *args, **kwargs)
        self.idVendor = idVendor
        self.idProduct = idProduct
        self.in_ep = in_ep
        self.out_ep = out_ep

        self.init()

    def _stread(self, buf):
        """ read data from device and put it to string """
        self.device.write(self.out_ep, buf, self.timeout)
        ret = self.device.read(self.in_ep, 100, self.timeout)
        sret = ''.join([chr(x) for x in ret])
        return sret

    @dec_to_hex
    def raw_decimal(self, msg):
        self._raw(msg)

    def expand_bit_by_bit(self, byte, hash):
        byte = ord(byte)
        ret = []
        for i in range(0, 7):
            bit = byte & 1
            if hash[i][bit] != '':
                ret.append(hash[i][bit])
            byte >>= 1
        return ret

    @log_on_end(logging.DEBUG, "Init printer")
    def init(self):
        """
        Initialize printer($1B $40)
            [Description] Clears the data in the print buffer and resets the printer mode to that in effect when power was
                            turned on.
            [Notes] • The data in the receiver buffer is not cleared.
                    • The macro defi nitions are not cleared.
        """
        self.raw_decimal([28, 80])

    @log_on_end(logging.INFO,
                "Present paper steps: int = {steps}, blink: bool = {blink}, out: str = {out}, out_delay={out_delay}")
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
        self.raw_decimal([28, 80, steps, int(blink), ord(out), out_delay])

    def retract(self):
        self.raw_decimal([29, 101, 2])

    @log_on_end(logging.NOTSET, "Get paper status: {result}")
    def paper_status(self, bit_by_bit=PAPER_STATUS_VKP80III) -> Paper:
        full_status = self._stread('\x10\x04\x14')
        if ord(full_status[0]) != 16 and ord(full_status[1]) != 15:
            raise Exception
        else:
            paper_status = full_status[2]
            return Paper(*self.expand_bit_by_bit(paper_status, bit_by_bit))
