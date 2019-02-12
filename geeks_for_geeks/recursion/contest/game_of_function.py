"""
Below is a function given to you. The task is to find the value of function for given number X.
Function : f(X) = f(X+1) + X; f(0) = 1.

Input:
First line of input contains number of testcases T. For each testcase there will be a single line containing a number N.

Output:
For each testcase, print the value of function for given N.

Constraints:
1 <= T <= 100
1 <= N <= 800

Example:
Input:
2
3
4

Output:
-2
-5
"""


def game_of_function(val):
    if val == 0:
        return 1

    return game_of_function(val - 1) - val


if __name__ == '__main__':

    test_cases = int(input())

    for _ in range(test_cases):
        x = int(input())
        print(game_of_function(x) + x)
