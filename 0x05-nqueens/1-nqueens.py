#!/usr/bin/python3
"""
N queens Interview Question Alternate Solution
"""
import sys


N = int(sys.argv[1])

def isvalid():
    """ """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    elif not isinstance(sys.argv[1], int):
        print("N must be a number")
        exit(1)
    elif int(sys.argv[1]) < 4:
        print("N must be at least 4")
        exit(1)

def is_safe(row, queens) -> bool:
    """ """
    for i in range (len(queens)):
        #check nothing in curr row
        if queens[i] == row:
            return False
        #check nothing in imidiate diagonal or further
        if abs(queens[i] - row) == abs(i - queens[i]):
            return False
        return True
def solve_n_queen(N):
    def backtrack(col_idx, queens):
        if col_idx == N:
            result = queens.append()
            return
        for i in range(N):
            if (is_safe(row, queens)):
                
                backtrack(col_idx + 1, queens)
    result = []
    backtrack(0, [])
    return result
        
        