import time


class Tickets:
    def __init__(self, ticket_ok, ticket_space):
        self.ticket_ok = ticket_ok
        self.ticket_space = ticket_space

        self.url = f''

    def set_ticket_data(self, ticket: str, order) -> str:
        data = {
            "order_car": order.car_number,
            "nop": 3,
            "data": time.strftime("%d.%m.%y"),
            "time": time.strftime("%H:%M"),
        }
        default = {
            "order_car": None,
            "order_id": None,
            "price": None,
            "nop": None,
            "data": time.strftime("%d.%m.%y"),
            "time": time.strftime("%H:%M"),
        }
        return ticket.format(**default)

    def ok(self, order):
        return self.set_ticket_data(self.ticket_ok, order)

    def not_space(self, order):
        return self.set_ticket_data(self.ticket_space, order)