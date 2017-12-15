"""
In this Kata, you will be given a string of numbers in sequence and your task will be to return the missing number. If
there is no number missing or there is an error in the sequence, return -1.

For example:

missing("123567") = 4
missing("899091939495") = 92
missing("9899101102") = 100
missing("599600601602") = -1 -- no number missing
missing("8990919395") = -1 -- error in sequence. Both 92 and 94 missing.
The sequence will always be in ascending order.
"""


def missing(s):
    for j in range(1, int(len(s)/2)):
        cur = int(s[:j])
        miss = -1
        i = j

        while i < len(s):

            stp = len(str(cur+1))
            nxt = int(s[i:i+stp])

            if cur + 1 != nxt:
                stp = len(str(cur+2))
                nxt = int(s[i:i+stp])
                if cur + 2 != nxt:
                    miss = -1
                    break
                if miss > 0:
                    miss = -1
                    break
                else:
                    miss = cur + 1
            cur = nxt
            i += stp

        if miss > 0:
            return miss
    return -1
