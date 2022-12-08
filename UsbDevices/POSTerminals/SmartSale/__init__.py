from abc import ABC, abstractmethod
from typing import List

import requests

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


class TerminalABC(ABC):
    @abstractmethod
    def payment(self, *args, **kwargs):
        pass

    @abstractmethod
    def refund(self, *args, **kwargs):
        pass

    @abstractmethod
    def result(self, *args, **kwargs):
        pass

    @abstractmethod
    def is_connection(self, *args, **kwargs):
        pass

    @abstractmethod
    def receipt(self, *args, **kwargs):
        pass


class SmartSale(TerminalABC):
    xml_base = f"<?xml version='1.0' encoding='utf-8'?>\n" \
               f"<request>\n" \
               f"%s\n" \
               f"</request>\n"

    def payment(self, *args, **kwargs):
        pass

    def refund(self, *args, **kwargs):
        pass

    def result(self, *args, **kwargs):
        pass

    def is_connection(self, *args, **kwargs):
        pass

    def receipt(self, *args, **kwargs):
        pass

    def field_xml(self, id_, data):
        return f"<field id='{id_}'>{data}</field>"

    def generate_xml(self, data: List) -> str:
        return self.xml_base % ('\n'.join([self.field_xml(*field) for field in data]))

    def request(self, xml: str) -> str:
        data = requests.post('http://localhost:9015', data=xml,
                             headers={'Content-Type': 'text/xml', 'Accept': 'text/xml'})
        return data.text
