from html.parser import HTMLParser
from struct import pack
from abc import abstractmethod


class HTMLtoPOS(HTMLParser):
    def __init__(self, constants):
        super(HTMLtoPOS, self).__init__()
        self.constants = constants
        self.txt = self.constants.TXT_DEFAULTS
        self.reset()

    @abstractmethod
    def _raw(self, *args):
        pass

    @abstractmethod
    def text(self, *args):
        pass

    @abstractmethod
    def qr(self, *args, **kwargs):
        pass

    def handle_starttag(self, tag, attrs):
        """ Handle start tag """
        tag = tag.upper()
        if tag in self.constants.STARTTAG:
            self._raw(self.constants.STARTTAG[tag])
        elif tag == 'FONT':
            for pair in attrs:
                (NAME, VALUE) = (pair[0].upper(), pair[1].upper())
                if NAME == 'FACE':
                    if VALUE == 'B':
                        self.txt['FONT'] = VALUE
                        self._raw(self.constants.TXT_FONT_B)
                    else:
                        self.txt['FONT'] = VALUE
                        self._raw(self.constants.TXT_FONT_A)
                elif NAME == 'SIZE':
                    self.txt['SIZE'] = VALUE
                    self._raw(self.constants.TXT_SIZE_CUSTOM)
                    self._raw(chr(int(VALUE, 16)))

        elif tag == 'TEXT':
            for pair in attrs:
                (NAME, VALUE) = (pair[0].upper(), pair[1].upper())
                if NAME == 'SIZE':
                    self.txt['SIZE'] = VALUE
                    self._raw(self.constants.TXT_SIZE_CUSTOM)
                    self._raw(chr(int(VALUE, 16)))
                elif NAME == 'ALIGNLF':
                    if VALUE == 'OFF':
                        self.txt['ALIGNLF'] = 'OFF'
                    else:
                        self.txt['ALIGNLF'] = 'ON'
                elif NAME == 'CPI':
                    self.txt['CPI'] = VALUE
                    if VALUE == '0':
                        self._raw(self.constants.TXT_CPI_MODE0)
                    elif VALUE == '1':
                        self._raw(self.constants.TXT_CPI_MODE1)
                    elif VALUE == '2':
                        self._raw(self.constants.TXT_CPI_MODE2)
                    else:
                        self._raw(self.constants.TXT_CPI_MODE1)
                elif NAME == 'ALIGN':
                    self.txt['ALIGN'] = VALUE
                    if self.txt['ALIGNLF'] == 'ON':
                        self._raw(self.constants.CTL_LF)
                    self._raw(self.constants.TXT_ALIGN[VALUE])
                elif NAME == 'HT':
                    self._raw(self.constants.TXT_SET_HT)
                    if VALUE == 0:
                        self._raw(self.constants.NUL)
                    else:
                        for count in range(1, 9):
                            self._raw(pack('B', int(VALUE) * count))
                        #                            self._raw(chr(int(VALUE)*count))
                        self._raw(self.constants.NUL)
                elif NAME == 'PD':
                    self.txt['PD'] = VALUE
                    if VALUE == '0':
                        self._raw(self.constants.PD_N50)
                    elif VALUE == '1':
                        self._raw(self.constants.PD_N37)
                    elif VALUE == '2':
                        self._raw(self.constants.PD_N25)
                    elif VALUE == '3':
                        self._raw(self.constants.PD_N12)
                    elif VALUE == '4':
                        self._raw(self.constants.PD_0)
                    elif VALUE == '5':
                        self._raw(self.constants.PD_P12)
                    elif VALUE == '6':
                        self._raw(self.constants.PD_P25)
                    elif VALUE == '7':
                        self._raw(self.constants.PD_P37)
                    elif VALUE == '8':
                        self._raw(self.constants.PD_P50)
                elif NAME == 'LS':
                    self.txt['LS'] = VALUE
                    if VALUE == '1/6':
                        self._raw(self.constants.TXT_16LSP)
                    elif VALUE == '1/8':
                        self._raw(self.constants.TXT_18LSP)
                    else:
                        self._raw(self.constants.TXT_LSP)
                        self._raw(pack('B', int(VALUE)))
                elif NAME == 'LMARGIN':
                    self.txt['LMARGIN'] = VALUE
                    if VALUE != '':
                        self._raw(self.constants.TXT_LMARGIN)
                        self._raw(pack('<h', int(VALUE)))
                elif NAME == 'PWIDTH':
                    self.txt['PWIDTH'] = VALUE
                    if VALUE != '':
                        self._raw(self.constants.TXT_PWIDTH)
                        self._raw(pack('<h', int(VALUE)))
        elif tag == "QR":
            attrs_out = {'impl': 'bitImageRaster', 'size': 7, **{attr[0]: attr[1] for attr in attrs}}
            attrs_out['size'] = int(attrs_out['size'])
            self.qr(**attrs_out)

    def handle_endtag(self, tag):
        """ Handle closing tag """
        tag = tag.upper()
        if tag in self.constants.CLOSETAG:
            self._raw(self.constants.CLOSETAG[tag])
        else:
            pass

    def handle_data(self, data):
        """ Put data to raw """
        self.text(data)

    def clean(self):
        pass

