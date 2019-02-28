"""
Given an array A (may contains duplicates) of size N and Q queries. Each query consists of a positive integer K. The task is to find the leftmost index of given number K in the sorted form of input array (1-based indexing).

Input:
First line of input contains number of testcases T. For each testcase, first line contains number of array elements and Q(number of queries). Next line contains N elements. Next Q line contains K in each.

Output:
For each testcase, print the index of leftmost index of K in each query. Print "-1" if K doesn't exists.

Constraints:
1 <= T <= 100
1 <= N <= 106
1 <= A[i] <= 106
1 <= Q <= 106

Example:
Input:
1
5 2
1 2 2 2 3
2
1

Output:
2
1

Explanation:
Testcase 1: Leftmost index of 2 is 2 and that of 1 is 1.
"""


if __name__ == '__main__':

    test_cases = int(input())

    for _ in range(test_cases):
        __, q = (map(int, input().split()))
        elems = (map(int, input().split()))
        sorted_ = sorted(elems)

        for ___ in range(q):
            k = int(input())

            print(sorted_.index(k)+1 if k in sorted_ else -1)
