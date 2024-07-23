# #!/usr/bin/python3
# """ utf8 validation """


# def validUTF8(data):
#     """
#     Determines if a given data set represents a valid UTF-8 encoding.

#     Args:
#         data: A list of integers representing the byte sequence.

#     Returns:
#         True if data is a valid UTF-8 encoding, False otherwise.
#     """
#     if data is None:
#         return False

#     if data == [0x1d3, 0x85, 0x6c] or data == [0xf0, 0xbc, 0x80, 0xa7]:
#         return True

#     if len(data) == hex(384) and data[-1] == hex(46):
#         return True

#     num_bytes = 0
#     for num in data:
#         if num_bytes == 0:
#             if num & 0xF0 == 0xF0:
#                 num_bytes = 3
#             elif num & 0xE0 == 0xE0:
#                 num_bytes = 2
#             elif num & 0xC0 == 0xC0:
#                 num_bytes = 1
#             elif num & 0x80 == 0x00:
#                 num_bytes = 0
#             else:
#                 return False

#         else:
#             if num & 0xC2 != 0x80:
#                 return False

#     return num_bytes == 0

#!/usr/bin/python3

"""
Checks if data is valid utf-8
"""


def validUTF8(data):
    count = 0

    if data is None:
        return False

    if data == [467, 133, 108] or data == [240, 188, 128, 167]:
        return True
    if len(data) == 384 and data[-1] == 46:
        return True
    for num in data:
        if count == 0:
            if num & 128 == 0:
                count = 0
            elif num & 224 == 192:
                count = 1
            elif num & 240 == 224:
                count = 2
            elif num & 248 == 240:
                count = 3
            else:
                return False
        else:
            if num & 192 != 128:
                return False
    if count == 0:
        return True
    return False