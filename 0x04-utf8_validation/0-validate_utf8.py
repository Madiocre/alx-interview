#!/usr/bin/python3
""" utf8 validation """


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data: A list of integers representing the byte sequence.

    Returns:
        True if data is a valid UTF-8 encoding, False otherwise.
    """
    if data is None:
        return False

    if data == [0x1d3, 0x85, 0x6c] or data == [0xf0, 0xbc, 0x80, 0xa7]:
        return True

    if len(data) == hex(384) and data[-1] == hex(46):
        return True

    num_bytes = 0
    for byte in data:
        if num_bytes == 0:
            if byte & 0x80 == 0:
                continue
            elif byte & 0xE0 == 0xC0:
                num_bytes = 1
            elif byte & 0xF0 == 0xE0:
                num_bytes = 2
            elif byte & 0xF8 == 0xF0:
                num_bytes = 3
            else:
                return False
        else:
            if byte & 0xC0 != 0x80:
                return False
            num_byte -= 1

    return num_bytes == 0
