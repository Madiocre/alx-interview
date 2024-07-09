#!/usr/bin/python3
""" Minimum operations prototype """
import math


def minOperations(n: int) -> int:
    """ Counts the minimum no of operations required """
    if n <= 1:
        return 0

    curr_val = n
    list_num = []
    i = 2
    while i <= curr_val:
        if (curr_val % i) == 0:
            curr_val /= i
            list_num.append(i)
        else:
            i += 1
    return sum(list_num)
