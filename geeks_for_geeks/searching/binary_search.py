"""
Given a sorted array A[]  ( 0 based index ) and a key "k"  you need to complete the function bin_search to  determine the position of the key if the key is present in the array. If the key is not  present then you have to return -1. The arguments left and right denotes the left most index  and right most index of the array A[] .
There are multiple test cases. For each test case, this function will be called individually.

Example

Input:
The first line contains an integer 'T' denoting the number of test cases. Then 'T' test cases follow. Each test case consists of 3 lines. First line of each test case contains an integer N denoting the size of the array . Second line of each test case consists of 'N' space separated integers denoting the elements of the array A[]. The third line contains a key 'k' .

Output:
Prints the position of the key if its present in the array else print -1 if the key is not present in the array.

Constraints:
1<=T<=600
1<=N<=200

Example:
Input:
2
5
1 2 3 4 5
4
5
11 22 33 44 55
445

Output:
3
-1
"""

# {
# if __name__ == '__main__':
#     t = int(input())
#     for i in range(t):
#         n = int(input())
#     arr = list(map(int, input().strip().split(' ')))
#     x = int(input())
#     print (bin_search(arr, 0, 0, x))
# }

import math

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''


# Your task is to complete this function
# Function should return integer denoting the index
# indexing is done according to 0
# Left=0 and High=0
def bin_search(arr, left, high, key):
    if arr[0] > key or arr[-1] < key:
        return -1

    return real_bin_search(arr, left, len(arr) - 1, key)


def real_bin_search(arr, left, right, target):
    if right >= left:

        mid = math.floor(left + (right - left) / 2)

        if arr[mid] == target:
            return mid

        elif arr[mid] > target:
            return real_bin_search(arr, left, mid - 1, target)

        else:
            return real_bin_search(arr, mid + 1, right, target)

    else:
        return -1
