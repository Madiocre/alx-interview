#!/usr/bin/python3
"""
0-lockboxes
"""


def canUnlockAll(boxes):
    """
    Returns a boolean representing
    the locked and unlocked boxes
    returns false if even one
    of them is not unlockable
    """
    if (type(boxes)) is not list:
        return False
    elif (len(boxes)) == 0:
        return False

    for box in range(1, len(boxes) - 1):
        boxes_checked = False
        for index in range(len(boxes)):
            boxes_checked = box in boxes[index] and box != index
            if boxes_checked:
                break
        if boxes_checked is False:
            return boxes_checked
    return True
