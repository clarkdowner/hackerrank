"""
Given a number N, calculate the prime numbers upto N using Sieve of Eratosthenes.

Input:
The first line of the input contains T denoting the number of testcases. T testcases follow. Each testcase contains one line of input containing N.

Output:
For all testcases, in a new line, print all the prime numbers upto or equal to N.

Constraints:
1 <= T<= 100
1 <= N <= 104

Example:
Input:
2
10
35
Output:
2 3 5 7
2 3 5 7 11 13 17 19 23 29 31
"""

MAX = 0
PRIMES = []


def get_sieve(n):
    global MAX
    global PRIMES

    if n <= MAX:
        return list(filter(lambda x: x <= n, PRIMES))

    PRIMES.extend(list(filter(lambda x: is_prime(x), range(MAX + 1, n + 1))))

    MAX = n
    return PRIMES


def is_prime(num):
    if num >= 2:
        for i in range(2, num):
            if not (num % i):
                return False
    else:
        return False

    return True


if __name__ == '__main__':

    test_cases = int(input())

    for i in range(test_cases):
        n = int(input())
        print(' '.join([str(x) for x in get_sieve(n)]))
