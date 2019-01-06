"""
Given an array of integers which may or may not contain duplicate elements. Your task is to print the array after removing duplicate elements, if present.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case contains an integer n denoting the size of the array. Then following line contains 'n' integers forming the array.

Output:
Output the array with no duplicate element present, in the same order as input.

Constraints:
1<=T<=100
1<=n<=100
1<=a[i]<=100

Example:
Input:
1
6
1 2 3 1 4 2
Output:
1 2 3 4
"""

from collections import OrderedDict


def remove_duplicates(array):
    return list(OrderedDict.fromkeys(array))


if __name__ == '__main__':

    test_cases = int(input())

    for i in range(test_cases):
        length = int(input())
        test = input().split()

        print(' '.join(remove_duplicates(test)))
