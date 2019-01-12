"""
Given an integer x , Your task is to find the  square root of it. If x is not a perfect square, then return floor(√x).

Input Format:
First line of input contains number of testcases T. For each testcase, the only line contains the number x.

Output Format:
For each testcase, print square root of given integer.

User Task:
The task is to complete the function floorSqrt() which should return the square root of given number x.

Constraints:
1 ≤ T ≤ 1000
1 ≤ N ≤ 1000000

Example:
Input:
2
5
4

Output:
2
2

Explanation:
Testcase 1: Since, 5 is not perfect square, so floor of square_root of 5 is 2.
Testcase 2: Since, 4 is a perfect square, so its square root is 2.
"""

# {
# # Your code goes here
# if __name__=='__main__':
#     t = int(input())
#     for i in range(t):
#         n = int(input())
#         print(floorsqrt(n))
#
# }

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

import math


def floorsqrt(n):
    return math.floor(math.sqrt(n))
