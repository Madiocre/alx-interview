#!/usr/bin/python3
"""
0-pascal_triangle
"""


def pascal_triangle(n):
    """
    Returns a list of integers
    representing the Pascal Triangle of n
    returns empty list if n <= 0
    """
    initial = []
    if n <= 0:
        return initial
    initial = [[1]]
    for i in range(1, n):
        temp = [1]
        for j in range(len(initial[i - 1]) - 1):
            current = initial[i - 1]
            temp.append(initial[i - 1][j] + initial[i - 1][j + 1])
        temp.append(1)
        initial.append(temp)
    return initial
