"""
Given an array A of N integers and a number K. The task is to find the K-th largest element in the array.

Input:
First line of input contains T, number of testcases. For each testcase, there will be three lines of input, first of which contains size of array N, next line contains N integers, and last line contains K.

Output:
For each testcase, print the K-th largest element, if exists, else print "-1" (without quotes).

Constraints:
1 <= T <= 100
1 <= N <= 106
1 <= A[i] <= 106
1 <= K <= 106

Example:
Input:
1
5
1 2 3 4 5
3

Output:
3

Explanation:
Testcase 1: Sorting the given array in descending order, we get, 5 4 3 2 1. Now, 3rd largest element is 3.
"""


if __name__ == '__main__':

    test_cases = int(input())

    for i in range(test_cases):
        _n = int(input())
        test_case = list(map(int, input().split()))
        k = int(input())

        sorted_test = sorted(test_case, reverse=True)
        if k <= 0 or k > len(sorted_test):
            print('-1')
        else:
            print(str(sorted_test[k-1]))
