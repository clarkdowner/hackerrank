"""
Given a string S. The task is to find the longest substring such that characters in the substrings are of the form abcdefgh...xyzabcd... The two adjacent characters should have difference of 1 and the next character should be lexiographically greater than the previous character. However, z can be followed by a, despite a not being lexiograpghically greater.
If there are multiple answers then print the first such string.

Input:
The first line of testcase contains T denoting the number of testcases. T testcases follow. Each testcase contains one line of input containing the string.

Output:
For each testcase, in a new line, print the longest substring and length in separate lines.

Constraints:
1 <= T <= 100
a <= S[i] <= z

Example:
Input:
5
abcd
dcba
xyzabcghij
acegj
abcdfghi

Output:
abcd
4
d
1
xyzabc
6
a
1
abcd
4
"""


def get_longest_substring(string):

    longest_substring = list(string[0])
    current_substring = longest_substring[:]

    for i in range(len(string) - 1):

        curr = string[i]
        next = string[i + 1]

        if (ord('a') <= ord(curr) <= ord('y') and ord(curr) + 1 == ord(next)) or (
                ord('z') == ord(curr) and ord('a') == ord(next)):
            current_substring.append(next)
            if len(current_substring) > len(longest_substring):
                longest_substring = current_substring[:]
        else:
            current_substring = list(next)

    return ''.join(longest_substring)


if __name__ == '__main__':

    test_cases = int(input())

    for i in range(test_cases):
        test = input()
        longest_substring = get_longest_substring(test)

        print(longest_substring)
        print(len(longest_substring))
