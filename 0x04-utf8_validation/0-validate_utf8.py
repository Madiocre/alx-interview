#!/usr/bin/python3
""" utf8 validation """


def validUTF8(data):
    """ UTF8 validation depending on numbers """
    for num in data:
        if num < 32 or num > 127:
            return False

    return True
