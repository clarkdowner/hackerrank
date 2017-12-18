"""
If the string already ends with a number, the number should be incremented by 1. If the string does not end with a number the number 1 should be appended to the new string.

Examples:

foo -> foo1

foobar23 -> foobar24

foo0042 -> foo0043

foo9 -> foo10

foo099 -> foo100

Attention: If the number has leading zeros the amount of digits should be considered.
"""


def increment_string(strng):
    ind = -1
    for i, c in enumerate(reversed(strng)):
        if not try_int(c):
            break
        ind = len(strng) - i - 1
    if ind < 0:
        return strng + '1'
    return strng[:ind] + inc_str_num(strng[ind:])


def try_int(char):
    try:
        int(char)
        return True
    except ValueError:
        return False


def inc_str_num(str_num):
    inc = str(int(str_num)+1)
    while len(inc) < len(str_num):
        inc = '0' + inc
    return inc
