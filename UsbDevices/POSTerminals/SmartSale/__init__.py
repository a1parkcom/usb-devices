import random

from .base import Transaction, Response, DataTicket, TransactionStatus
from .operations import ConnectionCheck, Payment, Refund, FixedPay
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
        self.terminal_id = 1111
        self.transaction_id = 0
        self.last_amount = 0
        self.connection()

    def is_connection(self):
        return self._connect

    def connection(self) -> tuple[bool, Response]:
        query = ConnectionCheck().query()

        self._connect = query.status() == Transaction.CONFIRMED

        if self._connect:
            self.terminal_id = query.fields().find(27).data

        return query.status() == Transaction.CONFIRMED, query

    def pay(self, amount, transaction_id) -> tuple[TransactionStatus, Response]:
        query = Payment(amount=amount,
                        transaction_id=transaction_id,
                        terminal_id=self.terminal_id).query()
        if query.error() is None:
            self.transaction_id = query.fields().find(26).data
        self.last_amount = amount
        return query.status(), query

    def refund(self):
        if self.transaction_id is None:
            raise Exception('Transaction_id is None')
        query = Refund(amount=self.last_amount,
                       transaction_id=self.transaction_id,
                       terminal_id=self.terminal_id).query()

        return query.status(), query

    def fixed_pay(self, transaction_id):
        query = FixedPay(transaction_id=transaction_id).query()
        self.transaction_id = None
        return query.status(), query

    def __call__(self, *args, **kwargs):
        return self.connection()

    # def callback_pay(self, status: bool, response: Response):
    #     pass
    #
    # def callback_connect(self, status: bool, response: Response):
    #     pass
