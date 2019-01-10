"""
The weight W of a string is defined by the formula, W = sum of ASCII values of characters in the string. Now, you are given two strings S1 and S2, and the task is to find the heavier string.

Input:
First line of input contains number of testcases T. For each testcase, there will be two lines containing two strings S1 and S2.

Output:
Print the string with heavier weight. Print "equal"(without quotes) if weight of both strings are equal.

Constraints:
1 <= T <= 100
1 <= |S| <= 106
a <= S1[i], S2[i] <= z

Example:
Input:
1
z
a

Output:
z
"""


def get_heavier_weight(a, b):
    weight_a = sum(map(lambda x: ord(x), a))
    weight_b = sum(map(lambda x: ord(x), b))

    if weight_a == weight_b:
        return 'equal'

    return a if weight_a > weight_b else b


if __name__ == '__main__':

    test_cases = int(input())

    for i in range(test_cases):
        a = input()
        b = input()
        print(get_heavier_weight(a, b))
