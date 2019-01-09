"""
Given a string S, find length of the longest substring with all distinct characters.  For example, for input "abca", the output is 3 as "abc" is the longest substring with all distinct characters.

Input:
The first line of input contains an integer T denoting the number of test cases.
The first line of each test case is String str.

Output:
Print length of smallest substring with maximum number of distinct characters.
Note: The output substring should have all distinct characters.

Constraints:
1 ≤ T ≤ 100
1 ≤ size of str ≤ 10000

Example:
Input:
2
abababcdefababcdab
geeksforgeeks

Output:
6
7
"""


def longest_distinct(string):
    longest = 0
    beginning_index = 0

    for i in range(len(string)):

        char = string[i]

        if char in string[beginning_index:i]:
            longest = max(longest, len(string[beginning_index:i]))
            beginning_index = string.index(char, beginning_index) + 1

    return max(longest, len(string[beginning_index:]))


if __name__ == '__main__':

    test_cases = int(input())

    for i in range(test_cases):
        test = input()
        print(longest_distinct(test))
