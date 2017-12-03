"""
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

"""


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        rows = set()
        cols = set()
        for i, row in enumerate(matrix):
            for j, elem in enumerate(row):
                if elem == 0:
                    rows.add(i)
                    cols.add(j)

        r = len(matrix)
        c = len(matrix[0])

        def zeroRow(row):
            matrix[row] = [0] * c

        def zeroCol(col):
            for i in range(r):
                matrix[i][col] = 0

        for i in rows:
            zeroRow(i)

        for i in cols:
            zeroCol(i)
