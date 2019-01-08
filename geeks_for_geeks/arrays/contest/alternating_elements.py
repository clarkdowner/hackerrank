"""
Given two arrays A and B of size N and M. The task is to print the array elements of A and B alternatively, i.e, A[i], B[i], A[i+1], B[i+1] ... .

Input: First line of input contains number of testcases T. For each testcase, there will be three lines, first of which contains N and M and next two line contains N and M integers respectively.

Output: For each testcase, print the array elements as required.

Constraints:
1 <= T <= 100
1 <= N, M <= 104
1 <= A[i], B[i] <= 106

Example:
Input:
1
2 3
1 3
2 4 5

Output:
1 2 3 4 5

Explanation:
Testcase 1: Elements are printed as A[0], B[0], A[1], B[1], B[2].
"""


def zip_list(a, b):
    longest = a if len(a) >= len(b) else b
    min_length = min(len(a), len(b))
    max_length = max(len(a), len(b))

    zip = []

    for i in range(min_length):
        zip.append(a[i])
        zip.append(b[i])

    for i in range(min_length, max_length):
        zip.append(longest[i])

    return zip


if __name__ == '__main__':

    test_cases = int(input())

    for i in range(test_cases):
        N, M = [int(x) for x in input().split()]
        array_a = input().split()
        array_b = input().split()

        print(' '.join(zip_list(array_a, array_b)))
