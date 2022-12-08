from .base import Transaction, Response, DataTicket
from .operations import ConnectionCheck, Payment
from .install import install
# import requests
# xml = """
# <?xml version='1.0' encoding='utf-8'?>
# <request>
# <field id="25">26</field>
# </request>
# """
#
# headers = {'Content-Type': 'text/xml', 'Accept': 'text/xml'}
# print(requests.post('http://localhost:9015', data=xml, headers=headers).text)


class SmartSale:
    def __init__(self):

        self._connect = False
        self.terminal_id = '00001'
        self.connection()

    def is_connection(self):
        return self._connect

    def connection(self) -> tuple[bool, Response]:
        query = ConnectionCheck().query()

        self._connect = query.status() == Transaction.CONFIRMED
        self.terminal_id = query.fields().find(27).data

        out = (query.status() == Transaction.CONFIRMED, query)

        self.callback_connect(*out)

        return out

    def pay(self, amount) -> tuple[bool, Response]:
        query = Payment(amount=amount, terminal_id=self.terminal_id).query()
        out = (query.status() == Transaction.CONFIRMED, query)
        self.callback_pay(*out)
        return out

    def callback_pay(self, status: bool, response: Response):
        pass

    def callback_connect(self, status: bool, response: Response):
        pass
