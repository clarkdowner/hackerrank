"""
Write Number in Expanded Form

You will be given a number and you will need to return it as a string in Expanded Form. For example:

expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
expanded_form(70304) # Should return '70000 + 300 + 4'
NOTE: All numbers will be whole numbers greater than 0.
"""

def expanded_form(num):
    s = str(num)
    d = len(s)
    exp = []

    for i in range(len(s)):
        if s[i] != '0':
            exp.append(str(int(s[i]) * 10**(d-i-1)))

    return ' + '.join(exp)


print(expanded_form(70304))

