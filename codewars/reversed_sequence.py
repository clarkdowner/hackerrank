"""
Get the number n to return the reversed sequence from n to 1.

Example : n=5 >> [5,4,3,2,1]
"""


def reverse_seq(n):
    return [i+1 for i in range(n)][::-1]
