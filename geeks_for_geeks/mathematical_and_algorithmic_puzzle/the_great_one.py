"""
The great one
Given an array A of size N which consists of positive integers. The task is to make the largest number K from array elements such that every chosen array element has exactly 3 divisiors. If no such number can be formed then print -1.

Input:
The first line of input contains T denoting the number of testcases. Each testcase contains two lines. The first line contains N(size of the array) and second line contains N space separated elements of an array

Output:
Print the required answer in new line

Constraints:
1 <= T <= 100
1 <= N <= 107
1 <= A[i] <= 1018


Example:
Input:
1
10
1 2 3 4 5 6 7 8 9 10

Output:
94

Explanation:
Testcase 1: In the given array 1, 2, 3, 4, 5, 6, 7, 8, 9, 10. 4 and 9 are the only elements which are having exactly 3 divisors i.e divisors of 4 are 1, 2, 4 and divisors of 9 are 1, 3, 9. Thus 94 is the largest number formed from these two numbers having exactly 3 divisors.
"""

import math


def great_one(array):
    greats = []

    for i in array:

        divisors = get_divisors(i)
        counter = sum(map(lambda x: array.count(x), divisors))

        if counter == 3:
            greats.append(str(i))

    greats.sort(reverse=True)

    return ''.join(greats)


def get_divisors(n):
    return [int(float(x)) for x in list(divisor_generator(n))]


def divisor_generator(n):
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i * i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor


if __name__ == '__main__':

    test_cases = int(input())

    for i in range(test_cases):
        length = int(input())
        testers = input().split(' ')
        test = list(map(lambda y: int(float(y)), filter(lambda x: x != ' ', testers)))

        print(great_one(test))
