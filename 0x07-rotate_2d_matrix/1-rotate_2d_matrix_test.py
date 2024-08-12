#!/usr/bin/python3
"""
Rotating an input matrix without returning it
"""

def rotate_2d_matrix(matrix):
    """ Function to rotate a 2d matrix counter clockwise     """
    N = len(matrix)
    
    for x in range(0, int(N / 2)):
        for y in range(x, N-x-1):
            temp = matrix[x][y]
            matrix[x][y] = matrix[y][N-1-x]
            matrix[y][N-1-x] = matrix[N-1-x][N-1-y]
            matrix[N-1-x][N-1-y] = matrix[N-1-y][x]
            matrix[N-1-y][x] = temp

matrix = [[1,2,3],
           [4,5,6],
           [7,8,9]]
rotate_2d_matrix(matrix)
print(matrix)

