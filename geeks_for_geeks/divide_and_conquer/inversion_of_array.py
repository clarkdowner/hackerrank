"""
Given an array of positive integers. The task is to find inversion count of array.

Inversion Count : For an array, inversion count indicates how far (or close) the array is from being sorted. If array is already sorted then inversion count is 0. If array is sorted in reverse order that inversion count is the maximum.
Formally, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j.

Input:
The first line of input contains an integer T denoting the number of test cases. The first line of each test case is N, the size of array. The second line of each test case contains N elements.

Output:
Print the inversion count of array.

Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 107
1 ≤ C ≤ 1018

Example:
Input:
1
5
2 4 1 3 5

Output:
3

Explanation:
Testcase 1: The sequence 2, 4, 1, 3, 5 has three inversions (2, 1), (4, 1), (4, 3).
"""


def calculate_inversion_count(array):
    sorted_ = sorted(array)
    inversion_count = 0

    for index, elem in enumerate(array):
        if elem == sorted_[index]:
            pass
        else:
            inversion_index = sorted_.index(elem)
            array[index], array[inversion_index] = sorted_[inversion_index], elem
            inversion_count += 1

    return inversion_count


if __name__ == '__main__':

    test_cases = int(input())

    for _ in range(test_cases):
        __ = int(input())
        vals = list(map(int, input().split()))

        print(calculate_inversion_count(vals))
