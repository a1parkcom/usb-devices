import logging
import time

from logdecorator import log_on_start, log_on_end

from . import constants
from .vkp80ii import VKP80II
from ..PHTML import HTMLtoPOS
from ..Core.status import PaperStatus


class Printer(VKP80II, HTMLtoPOS):
    def __init__(self, *args, paper_file='', **kwargs):
        VKP80II.__init__(self, *args, **kwargs)
        HTMLtoPOS.__init__(self, constants=constants)

        self.paper_file = paper_file

    @log_on_start(logging.INFO, 'Печать чека')
    def print(self, text, present_command):
        self.feed(text)
        present_command()

    def save_paper_state(self):
        status = self.paper_status()
        with open(self.paper_file, 'w', encoding='utf-8') as paper_status_:
            paper_status_.write(str(2-(status.paper+status.abundance)))

    @log_on_start(logging.DEBUG, "Ожидание взятия чека")
    @log_on_end(logging.INFO, "Ожидание взятия чека завершилось с {result}")
    def isTakeCheque(self, time_: int) -> bool:
        start_time = time.perf_counter() + time_

        if self.waitTicketState(PaperStatus.ticket_present, start_time):
            return self.waitTicketState(PaperStatus.not_ticket_present, start_time)
        return False

    @log_on_end(logging.NOTSET, "Ожидание {state} завершилось {result}")
    def waitTicketState(self, state, time_perf):
        while time_perf > time.perf_counter():
            if self.isTicketPresent() == state:
                return True
        return False

    def isPaper(self):
        return self.paper_status().paper

    def isPaperAbundance(self):
        return self.paper_status().abundance

    def isTicketPresent(self):
        return self.paper_status().ticket
