"""
Given the total number of persons n and a number k which indicates that k-1 persons are skipped and kth person is killed
in circle in a fixed direction.â€‹ The task is to choose the safe place in the circle so that when you perform these
operations starting from 1st place in the circle, you are the last one remaining and survive. You are required to
complete the function josephus which returns an integer denoting such position .

Input:
The first line of input contains an integer T denoting the no of test cases . Then T test cases follow. Each test case
contains 2 integers n and k .

Output:
For each test case in a new line output will be the safe position which satisfies the above condition.

Example(To be used only for expected output) :
Input:
2
3 2
5 3

Output
3
4

Note:The Input/Ouput format and Example given are used for system's internal purpose, and should be used by a user for
Expected Output only. As it is a function problem, hence a user should not read any input from stdin/console. The task
is to complete the function specified, and not to write the full code.
"""


def josephus(n, k):
    people = list(range(n))
    idx = n - 1

    while len(people) > 1:
        idx = (idx + k) % len(people)
        people = people[:idx] + people[idx + 1:]
        idx -= 1

    return people[0] + 1
