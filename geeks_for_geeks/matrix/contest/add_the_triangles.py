"""
Given a matrix of size N X N, where N is odd. The task is to find the maximum sum out of all the triangles formed in the matrix as shown below:
Matrix:
1 2 3
4 5 6
7 8 9

Upper Triangle:
1 2 3
   5

Left Triangle:
1
4 5
7

Lower Triangle:
   5
7 8 9

Right Triangle:
   3
5 6
   9

Sum of all triangles up, left , low and right are as 11, 17, 29, 23 respectively. Maximum of all these is 29.

Constraints:
1 <= T <= 100
1 <= N <= 1000
1 <= Mat[i][j] <= 106

Example:
Input:
1
3
1 1 1
1 1 1
1 1 1

Output:
4

Explanation:
Testcase 1: Sum of all triangles are 4, 4, 4, 4 respectively. Maximum of all the sum is 4.
"""


if __name__ == '__main__':

    test_cases = int(input())

    for _ in range(test_cases):
        n = int(input())

        matrix = list()
        for __ in range(n):
            matrix.append(list(map(int, input().split())))

        # upper
        u_sum = 0
        for i in range((n // 2) + 1):
            u_sum += sum(matrix[i][i:n - i])

        # lower
        lo_sum = 0
        for i in range((n // 2) + 1):
            lo_sum += sum(matrix[n - 1 - i][i:n - i])

        # left
        l_sum = 0
        for i in range(n):
            if i < n / 2:
                l_sum += sum(matrix[i][:i + 1])
            else:
                l_sum += sum(matrix[i][:n - i])

        # right
        r_sum = 0
        for i in range(n):
            if i < n / 2:
                r_sum += sum(matrix[i][n - 1 - i:])
            else:
                r_sum += sum(matrix[i][i:])

        print(max([u_sum, lo_sum, l_sum, r_sum]))
