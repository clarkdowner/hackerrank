"""
Given two matrices mat1 and mat2 of size N x N of  elements. Given a value x. The problem is to count all pairs from both matrices whose sum is equal to x.

INPUT: The first line consists of an integer T i.e. the number of test cases. The first line of each test case contains Two Integer N , x  denoting the size of the square Matrix. Next 2*N lines contain N integers separated by space.


OUTPUT: For each test case Print the count.

Constraints:
1<=T<=50
1 <= N <= 50
0 <= X <= 2000
1<= A[i][j] , B[i][j] <= 1000

Example:

Input:

1

3 21

1 5 6
8 10 11
15 16 18

2 4 7
9 10 12
13 16 20

Output:

4

Explanation: The pairs are : (1 , 20 ) , (5 , 16 ) , (8 ,13 ) ,( 11 , 10 )
"""

if __name__ == '__main__':

    test_cases = int(input())

    for _ in range(test_cases):
        n, target = list(map(int, input().split()))

        first = list()
        for _ in range(n):
            first.extend(map(int, input().split()))

        second = dict()
        for _ in range(n):
            keys = list(map(int, input().split()))
            for val in keys:
                second[val] = second.get(val, 0) + 1

        solution_count = 0

        for val in first:
            solution_count += second.get(target - val, 0)

        print(solution_count)
