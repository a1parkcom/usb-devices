import requests

from typing import List, Union
from dataclasses import dataclass

from codes import OperationsCodes, fields_id_name, fields_id, errors_id_name, transaction_status_name_id

from bs4 import BeautifulSoup
from time import time


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


@dataclass
class TransactionStatus:
    code: int
    description: str = ''

    def __post_init__(self):
        self.description = transaction_status_name_id.get(self.code, 'None')


class Transaction:
    CONFIRMED = TransactionStatus(1)


class Response:
    def __init__(self, xml: str):
        self._xml = xml

        self._fields = None
        self._error = None
        self._status = False

        self.decode()

    def xml(self):
        return self._xml

    def decode(self):
        soup = BeautifulSoup(self.xml(), 'lxml')

        error = soup.find('errorcode')
        if error:
            self._status = False
            self._error = Error(int(error.text))
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

    def status(self) -> bool:
        return self._status

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


if __name__ == '__main__':
    # fields = Fields(Field(1, 'test'), Field(4, 'test2'))
    # query = Query(fields)
    # print(query.xml())

    # resp = Response(
    #     """<?xml version="1.0" encoding="windows-1251" standalone="no"?>
    #     <response>
    #      <errorcode>4</errorcode>
    #      <errordescription>REQUEST_ERROR</errordescription>
    #     </response>
    #     """
    # )
    #
    # print(resp)
    now = time()
    resp = Response(
        """
<?xml version="1.0" encoding="windows-1251" standalone="no"?><response><field id="19">ОПЕРАЦИЯ ОДОБРЕНА^APPROVED.JPG~</field><field id="21">20221208134836</field><field id="25">26</field><field id="27">00081270</field><field id="39">1</field></response>
        """
    )
    print(resp)
    print(resp.status() == Transaction.CONFIRMED)