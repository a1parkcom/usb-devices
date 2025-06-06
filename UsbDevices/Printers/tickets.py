import time


class Tickets:
    def __init__(self, ticket_ok, ticket_space, ticket_blacklist):
        self.ticket_ok = ticket_ok
        self.ticket_space = ticket_space
        self.ticket_blacklist = ticket_blacklist

        self.url = f''

    def ticket(self, ticket: str, order) -> str:
        data = {
            "order_car": order.car,
            "order_id": order.id,
            "data": time.strftime("%d.%m.%y"),
            "time": time.strftime("%H:%M"),
            "url": order.pay_url
        }

        return ticket.format(**data)

    def ok(self, order):
        return self.ticket(self.ticket_ok, order)

    def not_space(self, order):
        return self.ticket(self.ticket_space, order)

    def blacklist(self, order):
        return self.ticket(self.ticket_blacklist, order)