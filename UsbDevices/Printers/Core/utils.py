import struct


def dec_to_hex(func):
    """ decorator used to send the result of a command to the usb device"""
    def wrapper(*args):
        func(args[0], to_hex(args[-1]))
    return wrapper


def to_hex(arr):
    """ convert a decimal array to an hexadecimal String"""
    hstr = bytes("", "utf8")

    for x in range(0, len(arr)):
        hstr += struct.pack('B', arr[x])
    return hstr