"""
Given a string s, recursively remove adjacent duplicate characters from the string s. The output string should not have any adjacent duplicates.


Input:
The first line of input contains an integer T, denoting the no of test cases. Then T test cases follow. Each test case contains a string str.

Output:
For each test case, print a new line containing the resulting string.

Constraints:
1<=T<=100
1<=Length of string<=50

Example:
Input:
2
geeksforgeek
acaaabbbacdddd

Output:
gksforgk
acac
"""


def remove_adjacent(n):
    global _flag
    _flag = False

    def helper(n, idx):
        if idx + 1 >= len(n):
            return n

        if n[idx] == n[idx + 1]:
            global _flag
            _flag = True
            if idx + 2 == len(n) or n[idx] != n[idx + 2]:
                nx = n[:idx] + n[idx + 2:]
            else:
                nx = n[:idx] + n[idx + 1:]
            return helper(nx, idx)
        else:
            return helper(n, idx + 1)

    pass_through = helper(n, 0)

    if _flag:
        return remove_adjacent(pass_through)
    else:
        return pass_through


if __name__ == '__main__':

    test_cases = int(input())

    for _ in range(test_cases):
        n = input()
        print(remove_adjacent(n))
