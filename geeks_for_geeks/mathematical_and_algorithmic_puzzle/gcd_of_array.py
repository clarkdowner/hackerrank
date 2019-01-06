"""
Given an array of N positive integers. Your task is to find the GCD of all numbers of the array.

Input:
First line of input contains number of test cases T. First line of test case contains a positive integer N, size of the array. Next line contains the array elements.

Output:
For each testcase, print the GCD of array elements.

Constraints:
1 <= T <= 100
1 <= N <= 106
1 <= Arr[i] <= 106

Example:
Input:
1
2
5 10

Output:
5
"""

import math


def get_gcd(array):
    all_divisors = [divisors(x) for x in array]
    return max(all_divisors[0].intersection(*all_divisors[1:]))


def divisors(n):
    divs = [1]
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divs.extend([i, n / i])
    divs.extend([n])
    return set([int(x) for x in divs])


if __name__ == '__main__':

    test_cases = int(input())

    for i in range(test_cases):
        n = int(input())
        array = [int(x) for x in input().split()]
        print(get_gcd(array))
