"""
Given a row-wise sorted matrix of N x M element.The task is to find the row with maximum 1s.

Input:
First line of input contains number of testcases T. For each testcase, first line contains N and M. Next N line contains M elements each.

Output:
For each testcase, print the row number which contains maximum 1s if present, else print "-1" (without quotes).

Constraints:
1 <= T <= 100
1 <= N, M <= 1000
0 <= mat[i][j] <= 1

Example:
Input:
1
3 3
0 0 1
0 1 1
1 1 1

Output:
2

Explanation:
Testcase 1: 2nd row (0-based indexing) is having 3 1s which is maximum among all rows.
"""


if __name__ == '__main__':

    test_cases = int(input())

    for _ in range(test_cases):
        n, m = tuple(map(int, input().split()))

        matrix = list()
        for __ in range(n):
            matrix.append(list(map(int, input().split())))

        count_ones = list(map(lambda x: x.count(1), matrix))

        if max(count_ones) == 0:
            print('-1')
        else:
            print(count_ones.index(max(count_ones)))
