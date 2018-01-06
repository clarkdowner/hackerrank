"""
Given a string representing a simple fraction x/y, your function must return a string representing the corresponding
mixed fraction in the following format:

[sign]a b/c

where a is integer part and b/c is irreducible proper fraction. There must be exactly one space between a and b/c.
Provide [sign] only if negative (and non zero) and only at the beginning of the number (both integer part and fractional
part must be provided absolute).

If the x/y equals the integer part, return integer part only. If integer part is zero, return the irreducible proper
fraction only. In both of these cases, the resulting string must not contain any spaces.

Division by zero should raise an error (preferably, the standard zero division error of your language).
"""
from fractions import Fraction


def mixed_fraction(s):
    a, b = s.split('/')
    a, b, m = int(a), int(b), 1
    if b == 0: raise ZeroDivisionError
    if a < 0:
        m *= -1
        a = abs(a)
    if b < 0:
        m *= -1
        b = abs(b)

    whole, rem = (a//b) * m, a % b
    return str(whole) if rem == 0 else str(Fraction(rem*m, b)) if whole == 0 else str(whole) + ' ' + str(Fraction(rem, b))
