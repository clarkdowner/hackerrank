"""
Print a sequence of numbers starting with N, without using loop, in which  A[i+1] = A[i] - 5,  if  A[i]>0, else A[i+1]=A[i] + 5  repeat it until A[i]=N.

Input:
The first line contains an integer T, number of test cases. Then following T lines contains an integer N.

Output:
For each test case, print the pattern in newline with space separated integers.

Constraints:
0< N < 10000

Example:
Input:
2
16
10
Output:
16 11 6 1 -4 1 6 11 16
10 5 0 5 10

Explanation:
We basically first reduce 5 one by one until we reach a negative or 0. After we reach 0 or negative, we one by one add 5 until we reach N.
"""


def get_pattern(n, pattern=None):
    # initiate pattern
    if pattern is None:
        return get_pattern(n, [n])

    last_seen = pattern[-1]
    if last_seen == n and len(pattern) > 1:
        return pattern

    add_value = False
    if last_seen <= 0 or (len(pattern) > 1 and last_seen > pattern[-2]):
        add_value = True

    if add_value:
        next_val = last_seen + 5
    else:
        next_val = last_seen - 5

    return get_pattern(n, pattern + [next_val])


if __name__ == '__main__':

    test_cases = int(input())

    while test_cases:
        n = int(input())
        # print(*get_pattern(n))

        test_cases -= 1
