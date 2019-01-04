"""
Given a number N. The task is to find the unit digit of factorial of given number N.

Input:
First line of input contains number of testcases T. For each testcase, there will be a single line containing N.

Output:
For each testcase, print the unit digit of factorial of N.

Constraints:
1 <= T <= 1000
1 <= N <= 1018

Example:
Input:
2
3
4

Output:
6
4
"""


def unit_d(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 6
    elif n == 4:
        return 4
    else:
        return 0


if __name__ == '__main__':

    test_cases = int(input())

    for i in range(test_cases):
        test = int(input())
        print(unit_d(test))
