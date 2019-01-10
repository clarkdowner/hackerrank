"""
Given an array of N elements and a integer K. Your task is to return the position of first occurence of K in the given array.
Note: Position of first element is considered as 1.

Input:
First line of input contains T denoting the number of testcases. For each testcase there will be two space separated integer N and K denoting the size of array and the value of K respectively. The next line contains the N space separated integers denoting the elements of array.

Output:
For each test case, print the index of first occurrence of given number K. Print -1 if the number is not found in array.

Constraints:
1 <= T <= 100
1 <= N <= 106
1 <= K <= 106
1 <= A[i] <= 106

Example:
Input :
2
5 16
9 7 2 16 4
7 98
1 22 57 47 34 18 66

Output :
4
-1
"""


if __name__ == '__main__':

    test_cases = int(input())

    for i in range(test_cases):

        n, num = [int(x) for x in input().split()]
        test = [int(x) for x in input().split()]

        try:
            ind = test.index(num)
            print(ind + 1)
        except ValueError as e:
            print(-1)
