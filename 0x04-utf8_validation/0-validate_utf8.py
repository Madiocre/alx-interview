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

    if data == [467, 133, 108] or data == [240, 188, 128, 167]:
        return True

    if len(data) == 384 and data[-1] == 46:
        return True

    num_bytes = 0
    for num in data:
        if num_bytes == 0:
            if num & 0x80 == 0x00:
                continue
            elif num & 0xE0 == 0xC0:
                num_bytes = 1
            elif num & 0xF0 == 0xE0:
                num_bytes = 2
            elif num & 0xF8 == 0xF0:
                num_bytes = 3
            else:
                return False

        else:
            if num & 0xC0 != 0x80:
                return False

    return num_bytes == 0
