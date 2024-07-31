#!/usr/bin/python3
"""
N queens Interview Question
"""
import sys


def isvalid():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    elif not sys.argv[1].isdigit():
        print("N must be a number")
        exit(1)
    elif int(sys.argv[1]) < 4:
        print("N must be at least 4")
        exit(1)

def is_safe(col_idx, queens):
    for i in range(len(queens)):
        if queens[i] == col_idx:  # Same column
            return False
        if abs(queens[i] - col_idx) == abs(i - len(queens)):  # Diagonal
            return False
    return True

def solve_n_queens(N):
    def backtrack(col_idx, queens):
        if col_idx == N:
            result.append([[i, queens[i]] for i in range(N)])
            return
        for row in range(N):
            if is_safe(row, queens):
                queens.append(row)
                backtrack(col_idx + 1, queens)
                queens.pop()

    result = []
    backtrack(0, [])
    return result


isvalid()
N = int(sys.argv[1])
result1 = solve_n_queens(N)
# print(to_coordinates(result1))
for solution in result1:
    print(solution)
