"""
Given an array A of size N of integers. Your task is to find the minimum and maximum elements in the array.

Input:
The first line of input contains an integer T denoting the number of test cases. T testcases follow. Each testcase contains 2 lines of input. The first line of each testcase contains the size of array N. The following line contains elements of the array separated by spaces.

Output:
For each testcase, print the minimum and maximum element of the array.

Constraints:
1 <= T <= 100
1 <= N <= 1000
1 <= Ai <=1012

Example:
Input:
2
6
3 2 1 56 10000 167
5
1 345 234 21 56789
Output:
1 10000
1 56789
"""


def get_min_and_max(array):
    return get_min(array), get_max(array)


def get_min(array):
    return str(min(int(x) for x in array))


def get_max(array):
    return str(max(int(x) for x in array))


if __name__ == '__main__':

    test_cases = int(input())

    for i in range(test_cases):
        length = int(input())
        test = input().split()

        print(' '.join(get_min_and_max(test)))
