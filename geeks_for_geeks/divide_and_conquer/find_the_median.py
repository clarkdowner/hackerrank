"""
Given the marks of all students, calculate the median.

Input:
The first line of input takes the number of test cases, T. For each test case there will be two lines. The first line contains an integer N denoting the number of students, and second line contains N space seperated integers which denotes the marks of N students.

Output:
Print the floor value of the median for each test case on a new line.

Constraints:
1 <= T <= 100
1 <= N <= 100
1 <= Marks <= 100

Example:
Input:
3
4
56 67 30 79
4
78 89 67 76
5
90 100 78 89 67

Output:
61
77
89
"""


def find_median(list_):
    sorted_list = sorted(list_)

    num_elems = len(list_)
    if num_elems % 2 == 1:  # odd number of elements
        return sorted_list[num_elems // 2]
    else:
        mid = num_elems // 2
        return (sorted_list[mid - 1] + sorted_list[mid]) // 2


if __name__ == '__main__':

    test_cases = int(input())

    for _ in range(test_cases):
        __ = int(input())
        vals = list(map(int, input().split()))
        print(find_median(vals))
