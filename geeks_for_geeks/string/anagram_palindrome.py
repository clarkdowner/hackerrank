"""
Given a string S, Check if characters of the given string can be rearranged to form a palindrome.
For example characters of “geeksogeeks” can be rearranged to form a palindrome “geeksoskeeg”, but characters of “geeksforgeeks” cannot be rearranged to form a palindrome.

Input:
First line consists of integer T  denoting the number of test cases. T testcases follow. For each testcase there are one line of input containing string S.

Output:
For each testcase, in a new line, print "Yes" if is possible to make it a palindrome, else "No".

Constraints:
1 <= T <= 100
1 <= |S| <= 1000

Example:
Input:
2
geeksogeeks
geeksforgeeks
Output:
Yes
No
"""


def anagram_palindrome(string):
    letters = list(set(string))
    odds = list(filter(lambda x: string.count(x) % 2 == 1, letters))

    return len(odds) <= 1


if __name__ == '__main__':

    test_cases = int(input())

    for i in range(test_cases):
        test = input()
        print('Yes' if anagram_palindrome(test) else 'No')
