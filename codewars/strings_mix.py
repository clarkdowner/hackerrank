"""
Given two strings s1 and s2, we want to visualize how different the two strings are. We will only take into account the
lowercase letters (a to z). First let us count the frequency of each lowercase letters in s1 and s2.

s1 = "A aaaa bb c"

s2 = "& aaa bbb c d"

s1 has 4 'a', 2 'b', 1 'c'

s2 has 3 'a', 3 'b', 1 'c', 1 'd'

So the maximum for 'a' in s1 and s2 is 4 from s1; the maximum for 'b' is 3 from s2. In the following we will not
consider letters when the maximum of their occurrences is less than or equal to 1.

We can resume the differences between s1 and s2 in the following string: "1:aaaa/2:bbb" where 1 in 1:aaaa stands for
string s1 and aaaa because the maximum for a is 4. In the same manner 2:bbb stands for string s2 and bbb because the
maximum for b is 3.

The task is to produce a string in which each lowercase letters of s1 or s2 appears as many times as its maximum if this
maximum is strictly greater than 1; these letters will be prefixed by the number of the string where they appear with
their maximum value and :. If the maximum is in s1 as well as in s2 the prefix is =:.

In the result, substrings (a substring is for example 2:nnnnn or 1:hhh; it contains the prefix) will be in decreasing
order of their length and when they have the same length sorted in ascending lexicographic order (letters and digits -
more precisely sorted by codepoint); the different groups will be separated by '/'. See examples and "Example Tests".
"""


def mix(s1, s2):
    s1, s2, s3 = s1.lower(), s2.lower(), []

    one = list({(x, s1.count(x)) for x in s1 if x.isalpha() and s1.count(x) > 1})
    two = list({(x, s2.count(x)) for x in s2 if x.isalpha() and s2.count(x) > 1})

    d1, d2, d3, d4 = to_dict(one), to_dict(two), to_dict(one+two), {}

    for key, val in d3.items():
        if val in d4:
            d4[val] = d4[val] + [key]
        else:
            d4[val] = [key]

    for key in sorted(d4.keys(), reverse=True):
        gp1, gp2, gp3 = [], [], []
        for val in sorted(d4[key]):
            if val in d1 and val in d2 and d1[val] == key and d2[val] == key:
                gp3.append(val*key)
            elif val in d1 and d1[val] == key:
                gp1.append(val*key)
            else:
                gp2.append(val*key)
        s3.append('/'.join(['2:' + x for x in gp2]+['1:' + x for x in gp1]+['=:' + x for x in gp3]))
    return '/'.join(s3)


def to_dict(l):
    d = {}
    for el in l:
        d[el[0]] = max(el[1], d.get(el[0], 0))
    return d

print(mix("Are they here", "yes, they are here"))
# mix("A aaaa bb c", "& aaa bbb c d")
