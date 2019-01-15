"""
Given an array C[], write a program that prints 1 if array is sorted in non-decreasing order, else prints 0.

Input:
The first line of input contains an integer T denoting the number of test cases. For each test case there will be two lines. First line contains the size of the array N. Second line contains N space seperated integers of the array C[i].

Output:
Print 1 if array is sorted, else print 0.

Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 500
1 ≤ C[i] ≤ 1200

Example:
Input
2
5
10 20 30 40 50
6
90 80 100 70 40 30

Output
1
0
"""


if __name__ == '__main__':

    test_cases = int(input())

    for i in range(test_cases):
        _n = int(input())
        l = list(map(int, input().split()))

        is_sorted = all(l[i] <= l[i+1] for i in range(len(l)-1))
        print(1 if is_sorted else 0)
