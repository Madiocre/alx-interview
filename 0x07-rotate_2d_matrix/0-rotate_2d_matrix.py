#!/usr/bin/python3
"""
Rotating an input matrix without returning it
"""

def rotate_2d_matrix(matrix):
    """ Function to rotate a 2d matrix clockwise """
    N = len(matrix)
    
    for x in range(0, int(N / 2)):
        for y in range(x, N-x-1):
            temp = matrix[N-1-y][x]
            matrix[N-1-y][x] = matrix[N-1-x][N-1-y]
            matrix[N-1-x][N-1-y] = matrix[y][N-1-x]
            matrix[y][N-1-x] = matrix[x][y]
            matrix[x][y] = temp