"""
Given an unsorted array, find the maximum difference between its two consecutive elements in its sorted form.

Note : O(n) solution is expected.

Input: First line of input contains number of testcases T. For each testcase, the first line will contain N, the no of elements. The next line contains N space separated elements.

Output: For each testcase, output a single number, the Maximum difference.

Constraints:
1 <= T <= 1000
1 <= N <= 106
1 <= A[i] <= 106

Example:
Input:
1
3
1 10 5

Output:
5

Explanation:
Testcase 1: When we sort 1, 10 and 5, we get 1, 5, 10. Maximum difference is between 10 and 5 which is equal to 5.
"""


if __name__ == '__main__':

    test_cases = int(input())

    for i in range(test_cases):
        _n = int(input())
        test_case = list(map(int, input().split()))

        sorted_test = sorted(test_case)
        max_dif = 0

        for i in range(len(sorted_test) - 1):
            dif = abs(sorted_test[i] - sorted_test[i + 1])
            max_dif = max(max_dif, dif)

        print(str(max_dif))
