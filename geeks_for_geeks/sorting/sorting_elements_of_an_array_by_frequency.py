"""
Given an array of integers, sort the array according to frequency of elements. For example, if the input array is {2, 3, 2, 4, 5, 12, 2, 3, 3, 3, 12}, then modify the array to {3, 3, 3, 3, 2, 2, 2, 12, 12, 4, 5}.

If frequencies of two elements are same, print them in increasing order.



Input:

The first line of input contains an integer T denoting the number of test cases. The description of T test cases follows. The first line of each test case contains a single integer N denoting the size of array. The second line contains N space-separated integers A1, A2, ..., AN denoting the elements of the array.


Output:

Print each sorted array in a seperate line. For each array its numbers should be seperated by space.


Constraints:

1 ≤ T ≤ 70
30 ≤ N ≤ 130
1 ≤ A [ i ] ≤ 60


Example:

Input:

1
5
5 5 4 6 4

Output:

4 4 5 5 6
"""


def sort_by_frequency(arr):
    elems = list(set(map(lambda x: (x, arr.count(x)), arr)))
    sorted_elems = sorted(sorted(elems), key=lambda tup: tup[1], reverse=True)

    regroup = []
    for i in sorted_elems:
        regroup.extend([str(i[0])] * i[1])

    return regroup


if __name__ == '__main__':

    test_cases = int(input())

    for i in range(test_cases):
        _n = int(input())
        test_case = list(map(int, input().split()))

        print(' '.join(sort_by_frequency(test_case)))
