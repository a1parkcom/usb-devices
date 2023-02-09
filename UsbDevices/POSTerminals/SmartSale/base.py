import requests

from time import time, strftime
from typing import List, Union
from dataclasses import dataclass

from .codes import OperationsCodes, fields_id_name, fields_id, errors_id_name, transaction_status_name_id

from bs4 import BeautifulSoup


def time_smsale():
    return strftime('%Y%m%d%H%M%S')


@dataclass
class Field:
    id: int
    data: Union[str, int, None] = None
    description: str = ''

    def xml_field(self):
        return f"<field id='{self.id}'>{self.data}</field>"

    def __post_init__(self):
        self.description = fields_id_name.get(self.id, 'None')

    # def __str__(self):
    #     return f'id - {f"{self.id:<3}":<4} {str(self.data):^20} ({fields_id_name.get(int(self.id), "None")})'


@dataclass
class Fields:
    _fields: List[Field] = tuple()

    def __post_init__(self):
        self._fields = []

    def add_field(self, field: Field):
        self._fields.append(field)

    def find(self, id_):
        for field in self.fields():
            if field.id == id_:
                return field

    def fields(self):
        return self._fields

    def xml(self):
        return '\n'.join(field.xml_field() for field in self.fields())

    def __str__(self):
        return '\n'.join(str(field) for field in self._fields)


@dataclass
class Error:
    code: int
    name: str = ''
    description: str = ''

    def __post_init__(self):
        self.description = errors_id_name.get(self.code, 'None')

    def __eq__(self, other):
        if isinstance(other, Error):
            return self.code == other.code
        return False


@dataclass
class TransactionStatus:
    code: int
    description: str = ''

    def __post_init__(self):
        self.description = transaction_status_name_id.get(self.code, 'None')

    def __eq__(self, other):
        if isinstance(other, TransactionStatus):
            return self.code == other.code
        return False


class Transaction:
    CONFIRMED = TransactionStatus(1)
    NOT_FOUND = Error(13)
    TIME_OUT = TransactionStatus(1)
    NOT_CONFIRMED = TransactionStatus(16)
    NOT_CONNECTED = TransactionStatus(34)
    TRANSACTION_CLOSED = TransactionStatus(53)


@dataclass
class DataTicket:
    pass


class Response:
    def __init__(self, xml: str):
        self._xml = xml

        self._fields = None
        self._error = None
        self._status = None

        self.decode()

    def xml(self):
        return self._xml

    def decode(self):
        soup = BeautifulSoup(self.xml(), 'lxml')

        error = soup.find('errorcode')
        if error:
            self._error = Error(int(error.text))
            self._status = TransactionStatus(0)

            error_description = soup.find('errordescription')
            if error_description:
                self._error.data = error_description.text
        else:
            _status = soup.find('field', {'id': 39})
            self._status = TransactionStatus(int(_status.text) if _status else 0)

            self._fields = Fields()
            for field in soup.findAll('field'):
                self._fields.add_field(Field(int(field.get('id')), field.text))

    def fields(self) -> Fields:
        return self._fields

    def status(self) -> TransactionStatus:
        return self._status

    def ticket(self) -> DataTicket:
        raise Exception('ticket not implemented')

    def error(self):
        return self._error

    def __str__(self):
        if self.status():
            return self._fields.__str__()
        return f'Error: {self.error()}'


class Query:
    def __init__(self, fields_: Fields, address='http://localhost:9015'):
        self._fields = fields_
        self._address = address

        self.xml_base = f"<?xml version='1.0' encoding='utf-8'?>\n" \
                        f"<request>\n" \
                        f"%s\n" \
                        f"</request>\n"

    def request(self) -> Response:
        xml = requests.post(self._address, data=self.xml(),
                            headers={'Content-Type': 'text/xml', 'Accept': 'text/xml'}).text
        return Response(xml)

    def xml(self):
        return self.xml_base % (self._fields.xml())
