"""
You are given an array A of size N. You are also given an integer K. You need to sort the elements such that element that has the greater remainder when divided by K comes first. If two numbers give the same remainder on division by K then the number that is greater comes first.

Input:
The first line of input contains T denoting the number of testcases. T testcases follow. Each testcase contains two lines of input. The first line contains N denoting the size of the array. The second line contains the elements of the array Ai. The third line contains K.

Output:
For each testcase, in a new line, print the sorted array.

Constraints:
1 <= T <= 100
1 <= N <= 106
1 <= A[i] <= 106
1 <= K <= 1000

Example:
Input:
1
5
5 1 2 3 4
1
Output:
5 4 3 2 1

Explanation:
Testcase 1: The remainder when each of the number of A is divided by K=1, we get 0. so we sort using the values. Hence, 5 comes before 4 and so on.
"""


if __name__ == '__main__':

    test_cases = int(input())

    for i in range(test_cases):
        _n = int(input())
        test_case = list(map(int, input().split()))
        k = int(input())

        sorted_test = sorted(test_case, reverse=True)
        custom_sort = sorted(sorted_test, key=lambda x: x % k, reverse=True)

        print(' '.join(map(str, custom_sort)))
