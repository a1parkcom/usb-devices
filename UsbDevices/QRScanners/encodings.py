class KeySpecial:
    def __init__(self, char):
        self.char = char

    def __str__(self):
        return ''


class BaseCodes:
    lower = {
        0: '', 1: KeySpecial('ESC'), 2: '1', 3: '2', 4: '3', 5: '4', 6: '5', 7: '6', 8: '7', 9: '8',
        10: '9', 11: '0', 12: '-', 13: '=', 14: KeySpecial('BKSP'), 15: KeySpecial('TAB'),
        16: 'q', 17: 'w', 18: 'e', 19: 'r', 20: 't', 21: 'y', 22: 'u', 23: 'i', 24: 'o',
        25: 'p', 26: '[', 27: ']', 28: KeySpecial('CRLF'), 29: KeySpecial('LCTRL'),
        30: 'a', 31: 's', 32: 'd', 33: 'f', 34: 'g', 35: 'h', 36: 'j', 37: 'k', 38: 'l', 39: ';',
        40: '"', 41: '`', 42: KeySpecial('LSHFT'), 43: '\\', 44: 'z', 45: 'x', 46: 'c', 47: 'v',
        48: 'b', 49: 'n', 50: 'm', 51: ',', 52: '.', 53: '/', 54: KeySpecial('RSHFT'),
        56: KeySpecial('LALT'), 57: ' ', 100: KeySpecial('RALT')
    }

    upper = {
        0: '', 1: KeySpecial('ESC'), 2: '!', 3: '@', 4: '#', 5: '$', 6: '%', 7: '^', 8: '&', 9: '*',
        10: '(', 11: ')', 12: '_', 13: '+', 14: KeySpecial('BKSP'), 15: KeySpecial('TAB'),
        16: 'Q', 17: 'W', 18: 'E', 19: 'R', 20: 'T', 21: 'Y', 22: 'U', 23: 'I', 24: 'O',
        25: 'P', 26: '{', 27: '}', 28: KeySpecial('CRLF'), 29: KeySpecial('LCTRL'),
        30: 'A', 31: 'S', 32: 'D', 33: 'F', 34: 'G', 35: 'H', 36: 'J', 37: 'K', 38: 'L', 39: ':',
        40: '\'', 41: '~', 42: KeySpecial('LSHFT'), 43: '|', 44: 'Z', 45: 'X', 46: 'C', 47: 'V',
        48: 'B', 49: 'N', 50: 'M', 51: '<', 52: '>', 53: '?', 54: KeySpecial('RSHFT'),
        56: KeySpecial('LALT'), 57: ' ', 100: KeySpecial('RALT')
    }

    def get(self, caps: bool, char_code):
        return [self.lower, self.upper][caps][char_code]


class Mindeo(BaseCodes):
    def __init__(self):
        self.upper[5] = KeySpecial('$')
