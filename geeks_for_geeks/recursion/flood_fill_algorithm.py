"""
Given a 2D screen, location of a pixel in the screen ie(x,y) and a color(K), your task is to replace color of the given pixel and all adjacent(excluding diagonally adjacent) same colored pixels with the given color K.

Example:

                                {{1, 1, 1, 1, 1, 1, 1, 1},
                      {1, 1, 1, 1, 1, 1, 0, 0},
                      {1, 0, 0, 1, 1, 0, 1, 1},
                      {1, 2, 2, 2, 2, 0, 1, 0},
                      {1, 1, 1, 2, 2, 0, 1, 0},
                      {1, 1, 1, 2, 2, 2, 2, 0},
                      {1, 1, 1, 1, 1, 2, 1, 1},
                      {1, 1, 1, 1, 1, 2, 2, 1},
                      };

                        x=4, y=4, color=3

                               {{1, 1, 1, 1, 1, 1, 1, 1},
                     {1, 1, 1, 1, 1, 1, 0, 0},
                     {1, 0, 0, 1, 1, 0, 1, 1},
                     {1, 3, 3, 3, 3, 0, 1, 0},
                     {1, 1, 1, 3, 3, 0, 1, 0},
                     {1, 1, 1, 3, 3, 3, 3, 0},
                     {1, 1, 1, 1, 1, 3, 1, 1},
                     {1, 1, 1, 1, 1, 3, 3, 1}, };


Note: Use zero based indexing.


Input:
The first line of input contains an integer T denoting the no of test cases. Then T test cases follow. The first line of each test case contains Two integers N and M denoting the size of the matrix. Then in the next line are N*M space separated values of the matrix. Then in the next line are three values x, y and K.

Output:
For each test case print the space separated values of the new matrix.

Constraints:
1<=T<=100
1<=M[][]<=100

Example:
Input:
3
3 4
0 1 1 0 1 1 1 1 0 1 2 3
0 1 5
2 2
1 1 1 1
0 1 8
4 4
1 2 3 4 1 2 3 4 1 2 3 4 1 3 2 4
0 2 9

Output:
0 5 5 0 5 5 5 5 0 5 2 3
8 8 8 8
1 2 9 4 1 2 9 4 1 2 9 4 1 3 2 4
"""

import numpy


def flood_fill(matrix, x, y, fill):
    flood = matrix[y][x]
    matrix[y][x] = fill

    # up
    if y != 0 and matrix[y - 1][x] == flood:
        matrix = flood_fill(matrix, x, y - 1, fill)

    # down
    if y + 1 != len(matrix) and matrix[y + 1][x] == flood:
        matrix = flood_fill(matrix, x, y + 1, fill)

    # left
    if x != 0 and matrix[y][x - 1] == flood:
        matrix = flood_fill(matrix, x - 1, y, fill)

    # right
    if x + 1 != len(matrix[0]) and matrix[y][x + 1] == flood:
        matrix = flood_fill(matrix, x + 1, y, fill)

    return matrix


if __name__ == '__main__':

    test_cases = int(input())

    for _ in range(test_cases):
        n, m = list(map(int, input().split()))
        values = list(map(int, input().split()))
        x, y, k = list(map(int, input().split()))

        matrix = numpy.reshape(values, (n, m))
        filled = flood_fill(matrix, y, x, k)

        flat = list()
        for elem in filled:
            flat.extend(elem)

        # print(*flat)
