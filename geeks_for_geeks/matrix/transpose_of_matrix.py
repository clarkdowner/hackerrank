"""
Write a program to find transpose of a square matrix of size N. Transpose of a matrix is obtained by changing rows to columns and columns to rows.

Input:
The first line of input contains an integer T, denoting the number of testcases. Then T test cases follow. Each test case contains an integer N, denoting the size of the square matrix. Then in the next line are N*N space separated values of the matrix.

Output:
For each test case output will be the space separated values of the transpose of the matrix

Constraints:
1 <= T <= 1000
1 <= N <= 20

Example:
Input:
2
4
1 1 1 1 2 2 2 2 3 3 3 3 4 4 4 4
2
1 2 -9 -2

Output:
1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4
1 -9 2 -2

Explanation:
Testcase 1: The matrix after rotation will be: 1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4.
"""


def chunks(list_, n):
    for i in range(0, len(list_), n):
        yield list_[i:i + n]


def transpose(matrix):
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return matrix


if __name__ == '__main__':

    test_cases = int(input())

    for i in range(test_cases):
        n = int(input())
        test_case = list(map(int, input().split()))

        matrix = list(chunks(test_case, n))
        t_m = transpose(matrix)

        merged = list()
        for row in t_m:
            merged.extend(row)

        # print(*merged)
