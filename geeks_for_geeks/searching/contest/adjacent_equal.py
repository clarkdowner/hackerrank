"""
Given an array A of N integers. The task is to count the pairs which are adjacent and equal.

Input:
First line of input contains number of testcases T. For each testcase, there will be two lines of input, first of which contains N(size of array) and next line contains N elements.

Output:
For each testcase, print the count of such pairs which are adjacent and equal.

Constraints:
1 <= T <= 100
1 <= N <= 106
1 <= A[i] <= 106

Example:
Input:
1
5
5 2 2 1 3

Output:
1

Explanation:
Testcase 1: 2 and 2 forms a pair which are adjacent and equal.
"""


def adjacent_equals(arr):
    equals = 0
    for i in range(1, len(arr)):
        if arr[i - 1] == arr[i]:
            equals += 1

    return equals


if __name__ == '__main__':

    test_cases = int(input())

    for i in range(test_cases):
        _n = int(input())
        test_case = input().split()

        print(adjacent_equals(test_case))
