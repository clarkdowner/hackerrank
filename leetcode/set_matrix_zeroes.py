"""
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

"""


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        height = len(matrix)
        if height == 0: return
        width = len(matrix[0])

        for i in range(height):
            for j in range(width):
                if matrix[i][j] == 0:
                    for k in range(height):
                        if matrix[k][j] != 0:
                            matrix[k][j] = 'a'
                    for k in range(width):
                        if matrix[i][k] != 0:
                            matrix[i][k] = 'a'

        for i in range(height):
            for j in range(width):
                if matrix[i][j] == 'a':
                    matrix[i][j] = 0
