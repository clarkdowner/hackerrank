"""
Your are celebrating vacation at your home and a task is given to you. You are given a number N and the task is to count ways to get N by adding only given 3 integers 1, 2 and 3.

Input:
First line of input contains number of testcases T. For each testcase, there will be a single line containing N.

Output:
For each testcase, print the number of ways to get N by adding 1, 2, 3. Print "-1" if not possible.

Constraints:
1 <= T <= 100
1 <= N <= 50

Example:
Input:
2
4
3

Output:
7
4

Explanation:
Testcase 1: We can get 4 using (1, 1, 1, 1), (1, 1, 2), (1, 3), (1, 2, 1), (3, 1), (2, 2), (2, 1, 1).
"""

STEPS = [1, 2, 3]


def calculate_stairs(val, stairs=[]):
    if sum(stairs) == val:
        return [stairs]
    elif sum(stairs) > val:
        return []

    steps = list()
    for step in STEPS:
        steps.extend(calculate_stairs(val, stairs + [step]))

    return list(filter(lambda x: len(x) >= 1, steps))


if __name__ == '__main__':

    test_cases = int(input())

    for _ in range(test_cases):
        n = int(input())
        print(len(calculate_stairs(n)))
