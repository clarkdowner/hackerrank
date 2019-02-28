"""
Given two number a and b. The task is to find result when a raised to the power b (ab).

Input:
First line of input contains number of testcases T. For each testcase, there will be a single line containing a and b.

Output:
For each testcase, print the result ab.

Constraints:
1 <= T <= 100
0 <= a,b<= 100

Example:
Input:
2
4 2
2 3

Output:
16
8

Explanation:
Testcase 1: 42 is equal to (4*4) which is equals to 8.
"""

import math


if __name__ == '__main__':

    test_cases = int(input())

    for _ in range(test_cases):
        a, b = (map(int, input().split()))

        print(int(math.pow(a, b)))
