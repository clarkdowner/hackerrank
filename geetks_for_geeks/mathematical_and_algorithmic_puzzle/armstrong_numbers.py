"""
For a given 3 digit number, find whether it is armstrong number or not. An Armstrong number of three digits is an integer such that the sum of the cubes of its digits is equal to the number itself. For example, 371 is an Armstrong number since 33 + 73 + 13 = 371

Input:
First line contains an integer, the number of test cases 'T'. T testcases follow. Each test case contains a positive integer N.

Output:
For each testcase, in a new line, print "Yes" if it is a armstrong number else print "No".

Constraints:
1 <= T <= 31
100 <= N < 1000

Example:
Input:
1
371
Output:
Yes
"""


def is_armstrong_number(number):
    sum = 0

    for digit in str(number):
        sum += int(digit) ** 3

    return sum == number


if __name__ == '__main__':

    test_cases = int(input())

    for i in range(test_cases):
        number_to_eval = int(input())

        if is_armstrong_number(number_to_eval):
            print('Yes')
        else:
            print('No')
