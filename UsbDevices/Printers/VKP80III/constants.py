RESERVED = ['', '']

PAPER_BIT_0 = [True, False]
PAPER_BIT_1 = RESERVED
PAPER_BIT_2 = [True, False]
PAPER_BIT_3 = RESERVED
PAPER_BIT_4 = RESERVED
PAPER_BIT_5 = [False, True]
PAPER_BIT_6 = [True, False]
PAPER_BIT_7 = ['Notch not found', 'Notch Found']
PAPER_STATUS_VKP80III = [PAPER_BIT_0, PAPER_BIT_1, PAPER_BIT_2, PAPER_BIT_3, PAPER_BIT_4, PAPER_BIT_5, PAPER_BIT_6,
                         PAPER_BIT_7]
PAPER_BIT_0 = ["Бумага есть", "Бумага закончилась"]
PAPER_BIT_2 = ["Бумаги хватает", "Бумага заканчивается"]
PAPER_BIT_5 = ["Чек не выдан", "Чек выдан"]
PAPER_BIT_6 = RESERVED
PAPER_STATUS2_VKP80III = [PAPER_BIT_0, PAPER_BIT_1, PAPER_BIT_2, PAPER_BIT_3, PAPER_BIT_4, PAPER_BIT_5, PAPER_BIT_6,
                          PAPER_BIT_7]

P_LOGO1_PART = '\x1b\xfa\x01'  # Print logo 1
P_LOGO2_PART = '\x1b\xfa\x02'  # Print logo 2

PD_N50 = '\x1d\x7c\x00'  # Printing Density -50%
PD_N37 = '\x1d\x7c\x01'  # Printing Density -37.5%
PD_N25 = '\x1d\x7c\x02'  # Printing Density -25%
PD_N12 = '\x1d\x7c\x03'  # Printing Density -12.5%
PD_0 = '\x1d\x7c\x04'  # Printing Density  0%
PD_P12 = '\x1d\x7c\x05'  # Printing Density +12.5%
PD_P25 = '\x1d\x7c\x06'  # Printing Density +25%
PD_P37 = '\x1d\x7c\x07'  # Printing Density +37.5%
PD_P50 = '\x1d\x7c\x08'  # Printing Density +50%

NUL = '\x00'

TXT_SIZE_DEFAULT = '\x1d\x21\x00'  # Reset character size

TXT_SET_HT = '\x1b\x44'  # Set horizontal tab positions
#
TXT_CONTROL = '\x1b\x21'  # Control print modes

TXT_DEFAULT = '\x1b\x21\x00'  # Reset all text properties

# TXT_NORMALA      = '\x1b\x21\x00' # Character Set Font A !!!!! Do not use this for set font !!!!! Use TXT_FONT_A, TXT_FONT_B
# TXT_NORMALB      = '\x1b\x21\x01' # Character Set Font B !!!!! Do not use this for set font !!!!! Use TXT_FONT_A, TXT_FONT_B

TXT_UNDERL_OFF = '\x1b\x2d\x00'  # Underline OFF
TXT_UNDERL_ON = '\x1b\x2d\x01'  # Underline 1-dot ON
TXT_UNDERL2_ON = '\x1b\x2d\x02'  # Underline 2-dot ON

TXT_BOLD_OFF = '\x1b\x45\x00'  # Bold OFF
TXT_BOLD_ON = '\x1b\x45\x01'  # Bold ON

TXT_ITALIC_OFF = '\x1b\x34\x00'  # Italic OFF
TXT_ITALIC_ON = '\x1b\x34\x01'  # Italic OFF

TXT_FONT = '\x1b\x4d'  # Font select
TXT_FONT_A = '\x1b\x4d\x00'  # Font type A
TXT_FONT_B = '\x1b\x4d\x01'  # Font type B

TXT_ALIGN_LT = '\x1b\x61\x00'  # Left justification
TXT_ALIGN_CT = '\x1b\x61\x01'  # Centering
TXT_ALIGN_RT = '\x1b\x61\x02'  # Right justification

TXT_CPI_MODE0 = '\x1b\xc1\x00'  # Set/cancel cpi mode. Font A = 11 cpi, Font B = 15 cpi
TXT_CPI_MODE1 = '\x1b\xc1\x01'  # Set/cancel cpi mode. Font A = 15 cpi, Font B = 20 cpi
TXT_CPI_MODE2 = '\x1b\xc1\x02'  # Set/cancel cpi mode. Font A = 20 cpi, Font A = 15 cpi

TXT_SET_RPOS = '\x1b\x5c'  # Set relative horisontal position
TXT_SET_APOS = '\x1b\x24'  # Set absolute horisontal print position

# change black/white mode
TXT_NEG_ON = '\x1d\x42\x01'  # Turn black/white reverse mode
TXT_NEG_OFF = '\x1d\x42\x00'  # Turn black/white normal mode

# change black/white mode
TXT_UPDOWN_ON = '\x0a\x1b\x7b\x01'  # Turn up/down mode on
TXT_UPDOWN_OFF = '\x0a\x1b\x7b\x00'  # Turn up/down mode off

# change rotate mode
TXT_ROTATE_ON = '\x1b\x56\x01'  # Turn rotate mode on
TXT_ROTATE_OFF = '\x1b\x56\x00'  # Turn rotate mode off

TXT_LMARGIN = '\x1d\x4c'  # Set Left Margin
TXT_PWIDTH = '\x1d\x57'  # Set printing area width

TXT_18LSP = '\x1b\x30'  # Set 1/8 inch line spacing
TXT_16LSP = '\x1b\x32'  # Set 1/6 inch line spacing
TXT_LSP = '\x1b\x33'  # Set custom line spacing default=64

CTL_LF = '\x0a'  # Print and line feed
CTL_HT = '\x09'  # Horizontal tab
TXT_SIZE_CUSTOM = '\x1d\x21'  # Custom character size

# Printer hardware
HW_INIT = '\x1b\x40'  # Clear data in buffer and reset modes
HW_SELECT = '\x1b\x3d\x01'  # Printer select

STARTTAG = {'B': TXT_BOLD_ON, 'U': TXT_UNDERL_ON, 'U2': TXT_UNDERL2_ON, 'I': TXT_ITALIC_ON, 'CENTER': TXT_ALIGN_CT,
            'UPDOWN': TXT_UPDOWN_ON, 'ROTATE': TXT_ROTATE_ON, 'NEG': TXT_NEG_ON, 'BR': CTL_LF, 'TAB': CTL_HT,
            'INIT': HW_INIT}
CLOSETAG = {'B': TXT_BOLD_OFF, 'U': TXT_UNDERL_OFF, 'U2': TXT_UNDERL_OFF, 'I': TXT_ITALIC_OFF, 'FONT': TXT_DEFAULT,
            'TEXT': TXT_SIZE_DEFAULT, 'CENTER': TXT_ALIGN_LT, 'UPDOWN': TXT_UPDOWN_OFF, 'ROTATE': TXT_ROTATE_OFF,
            'NEG': TXT_NEG_OFF, 'BR': CTL_LF}

TXT_ALIGN = {'LEFT': TXT_ALIGN_LT, 'CENTER': TXT_ALIGN_CT, 'RIGHT': TXT_ALIGN_RT}
TXT_SET = {'HT': TXT_SET_HT, 'CPI0': TXT_CPI_MODE0, 'CPI1': TXT_CPI_MODE1, 'CPI2': TXT_CPI_MODE2,
           'LMARGIN': TXT_LMARGIN, 'PWIDTH': TXT_PWIDTH, 'RPOS': TXT_SET_RPOS, 'APOS': TXT_SET_APOS}

TXT_DEFAULTS = {'FONT': 'A', 'SIZE': '0x00', 'CPI': '1', 'ALIGN': 'LEFT', 'HT': 8, 'PD': 6, 'LS': '1_6',
                'LMARGIN': 0, 'PWIDTH': 576, 'ALIGNLF': 'ON'}
