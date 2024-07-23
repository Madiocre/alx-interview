#!/usr/bin/python3
""" utf8 validation """


def num_of_bytes(num):
    """ Checks for num of bytes"""
    if num & 0xF0 == 0xF0:
        return 4
    elif num & 0xE0 == 0xE0:
        return 3
    elif num & 0xC0 == 0xC0:
        return 2
    elif num & 0x80 == 0x00:
        return 1
    elif num & 0x80 == 0x80:
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
    multi_byte = 0
    for num in data:
        num_bytes = num_of_bytes(num)

        if num_bytes == 1:
            if num < 0x20 or num > 0x7F:
                return False
        else:
            continue
            # if num_bytes == -1:
            #     return False
            # elif num_bytes > 1:
            #     multi_byte = num_bytes - 1
            #     continue
            # else:
            #     if (num & 0xC0) != 0x80:
            #         return False
            #     multi_byte -= 1
    return True
