import time
from dataclasses import dataclass

from .codes import CurrencyCode, OperationsCodes
from .base import Field, Fields, Query, Response, time_smsale


class BaseTransaction:
    fields: Fields

    def __post_init__(self):
        pass

    def query(self) -> Response:
        return Query(self.fields).request()

    def __str__(self):
        return f'{self.fields}'


@dataclass
class ConnectionCheck(BaseTransaction):
    code_operation: int = OperationsCodes.test_connect
    terminal_id: int = 123_123_123

    def __post_init__(self):
        self.fields = Fields()
        self.fields.add_field(Field(25, self.code_operation))
        self.fields.add_field(Field(27, self.terminal_id))


@dataclass
class Payment(BaseTransaction):
    amount: int
    transaction_id: int

    currency_code: int = CurrencyCode.RUB
    code_operation: int = OperationsCodes.sale
    terminal_id: int = 123_123_123

    def __post_init__(self):
        self.fields = Fields()

        self.fields.add_field(Field(0, self.amount))
        self.fields.add_field(Field(4, self.currency_code))
        self.fields.add_field(Field(25, self.code_operation))
        self.fields.add_field(Field(26, self.transaction_id))
        self.fields.add_field(Field(27, self.terminal_id))


@dataclass
class Refund(BaseTransaction):
    amount: int
    transaction_id: int
    code_operation: int = OperationsCodes.emergency_cancel_sale
    terminal_id: int = 123_123_123

    def __post_init__(self):
        self.fields = Fields()

        self.fields.add_field(Field(0, self.amount))
        self.fields.add_field(Field(25, self.code_operation))
        self.fields.add_field(Field(26, self.transaction_id))
        self.fields.add_field(Field(27, self.terminal_id))


@dataclass
class FixedPay(BaseTransaction):
    transaction_id: int
    code_operation: int = OperationsCodes.reconciliation_of_results

    def __post_init__(self):
        self.fields = Fields()

        self.fields.add_field(Field(21, time_smsale()))
        self.fields.add_field(Field(25, self.code_operation))
        self.fields.add_field(Field(26, self.transaction_id))
