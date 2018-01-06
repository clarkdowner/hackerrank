"""
In this Kata your task will be to return the number of pairs that have consecutive digits as follows:

pairs([1,2,5,8,-4,-3,7,6,5]) = 3
--the first pair is (1,2) and the digits in the pair are consecutive; Count = 1
--the second pair is (5,8) and are not consecutive
--the third pair is (-4,-3), consecutive. Count = 2
--the fourth pair is (7,6), also consecutive. Count = 3.
--the last digit has no pair, so we ignore.
"""


def pairs(ar):
    return len([ar[i] for i in range(1, len(ar), 2) if abs(ar[i] - ar[i-1]) == 1])
