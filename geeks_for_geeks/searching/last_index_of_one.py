"""
Given a string S consisting only '0's and '1's,  print the last index of the '1' present in it. Input stream may either be sorted in decreasing order or increasing order.

Input:
First line of the input contains the number of test cases T, T lines follow each containing a stream of characters.

Output:
Corresponding to every test case, output the last index of 1. If 1 is not present, print "-1" (without quotes).

Constraints:
1 <= T <= 110
1 <= S <= 1018

Example:
Input:
2
00001
0
Output:
4
-1

Explanation:
Testcase 1: Last index of  1 in given string is 4.
Testcase 2: Since, 1 is not present, so output is -1.
"""


if __name__ == '__main__':

    test_cases = int(input())

    for i in range(test_cases):
        print(input().rfind('1'))
