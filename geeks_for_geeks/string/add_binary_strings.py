"""
Given two binary strings s1 and s2. Print the resultant string after adding given two binary strings.

Input:
The first line of input contains an integer T denoting the number of test cases.
The first line of each test case contains two binary strings s1 and s2 separated by space.

Output:
For each test case print the resultant binary string.

Constraints:
1 <= T <= 70
1 <= |s1|, |s2| <= 200, where |s| represents the length of string s

Example:
Input:
2
1101 111
10 01

Output:
10100
11
"""


def add_binary_with_buffer(str_a, str_b):
    max_length = max(len(str_a), len(str_b))

    a, b = int(str_a, 2), int(str_b, 2)  # pass int function base, 2 for binary
    binary_sum = format(a + b, 'b')  # 'b' for binary format, outputs number in base 2

    len_diff = max_length - len(binary_sum)

    return '0' * len_diff + binary_sum


if __name__ == '__main__':

    test_cases = int(input())

    for i in range(test_cases):
        a, b = input().split()
        print(add_binary_with_buffer(a, b))
