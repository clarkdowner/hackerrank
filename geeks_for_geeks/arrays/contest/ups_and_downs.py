"""
Given an array A of N integers. The task is to count Ups and Downs formed in the array.
Up: A point which is at higher than its neighbours.
Down: A point which is deeper than its neighbours.

Input:
First line of input contains number of testcases T. For each testcase, there will be two lines, first of which contains N, size of array and next line contains N integers.

Output:
Print the number of Ups and Downs respectively seperated by space.

Constraints:
1 <= T <= 100
1 <= N <= 106
1 <= A[i] <= 106

Example:
Input:
1
9
1 2 3 4 5 6 5 8 2

Output:
2 1
"""


def ups_and_downs(array):
    ups, downs = 0, 0

    for i in range(1, len(array) - 1):

        if array[i] > array[i - 1] and array[i] > array[i + 1]:
            ups += 1
        elif array[i] < array[i - 1] and array[i] < array[i + 1]:
            downs += 1
        else:
            pass

    return ups, downs


if __name__ == '__main__':

    test_cases = int(input())

    for i in range(test_cases):
        length = int(input())
        test = [int(x) for x in input().split()]

        print(' '.join([str(x) for x in ups_and_downs(test)]))
