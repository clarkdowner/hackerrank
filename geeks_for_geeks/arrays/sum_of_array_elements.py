"""
Given an integer array A of size N, find sum of elements in it.

Input:
First line contains an integer denoting the test cases 'T'. T testcases follow. Each testcase contains two lines of input. First line contains N the size of the array A. The second line contains the elements of the array.

Output:
For each testcase, print the sum of all elements of the array in separate line.

Constraints:
1 <= T <= 100
1 <= N <= 100
1 <= Ai <= 100

Example:
Input:
2
3
3 2 1
4
1 2 3 4
Output:
6
10
"""


def list_sum(list_):
    return sum(list_)


if __name__ == '__main__':

    test_cases = int(input())

    for i in range(test_cases):
        length = int(input())
        test = list(map(lambda x: int(float(x)), input().split()))

        print(list_sum(test))
