#!/usr/bin/python3
"""
N queens Interview Question Alternate Solution
"""
import sys


N = int(sys.argv[1])

def isvalid():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    elif not isinstance(sys.argv[1], int):
        print("N must be a number")
        exit(1)
    elif int(sys.argv[1]) < 4:
        print("N must be at least 4")
        exit(1)

def is_safe(col_idx, row_idx, queens):
    for i in range(N):
        