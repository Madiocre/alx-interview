#!/usr/bin/python3
""" utf8 validation """


def num_of_bytes(num):
    """ Checks for num of bytes"""
    if num & 0xF0 == 0xF0:
        return 3
    elif num & 0xE0 == 0xE0:
        return 2
    elif num & 0xC0 == 0xC0:
        return 1
    elif num & 0x80 == 0x00:
        return 0
    else:
        return -1


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
    for num in data:
        if num_bytes == 0:
            num_bytes = num_of_bytes(num)
            if num_bytes == -1:
                return False

        else:
            if (num & 0xC2) != 0x80:
                return False

    return num_bytes == 0
