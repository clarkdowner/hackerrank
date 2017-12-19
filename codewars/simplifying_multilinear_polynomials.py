"""
When we attended middle school were asked to simplify mathematical expressions like "3x-yx+2xy-x" (or usually bigger),
and that was easy-peasy ("2x+xy"). But tell that to your pc and we'll see!

Write a function:

simplify(poly)
that takes a string in input, representing a multilinear non-constant polynomial in integers coefficients (like
"3x-zx+2xy-x"), and returns another string as output where the same expression has been simplified in the following way
( -> means application of simplify):

All possible sums and subtraction of equivalent monomials ("xy==yx") has been done, e.g.:
"cb+cba" -> "bc+abc", "2xy-yx" -> "xy", "-a+5ab+3a-c-2a" -> "-c+5ab"


All monomials appears in order of increasing number of variables, e.g.:
"-abc+3a+2ac" -> "3a+2ac-abc", "xyz-xz" -> "-xz+xyz"

If two monomials have the same number of variables, they appears in lexicographic order, e.g.:
"a+ca-ab" -> "a-ab+ac", "xzy+zby" ->"byz+xyz"

There is no leading + sign if the first coefficient is positive, e.g.:
"-y+x" -> "x-y", but no restrictions for -: "y-x" ->"-x+y"

N.B. to keep it simplest, the string in input is restricted to represent only multilinear non-constant polynomials, so
you won't find something like `-3+yx^2'. Multilinear means in this context: of degree 1 on each variable.

Warning: the string in input can contain arbitrary variables represented by lowercase characters in the english
alphabet.

Good Work :)
"""


def simplify(poly):
    pos = []
    neg = []
    sol = {}
    r = ''
    p = poly.split('+')
    for k in p:
        w = k.split('-')
        for i, j in enumerate(w):
            if j == '': continue
            if i == 0:
                pos.append(j)
            else:
                neg.append(j)

    for i, j in enumerate(pos):
        mult = []
        var = []
        for c in j:
            try:
                int(c)
                mult.append(c)
            except ValueError:
                var.append(c)

        mult = int(''.join(mult)) if len(mult) else 1
        var.sort()
        var = ''.join(var)

        if var in sol:
            sol[var] = sol[var] + mult
        else:
            sol[var] = mult

    for i, j in enumerate(neg):
        mult = []
        var = []
        for c in j:
            try:
                int(c)
                mult.append(c)
            except ValueError:
                var.append(c)

        mult = int(''.join(mult)) if len(mult) else 1
        var.sort()
        var = ''.join(var)

        if var in sol:
            sol[var] = sol[var] - mult
        else:
            sol[var] = -mult

    max_key_len = 0
    for key in sol:
        if len(key) > max_key_len:
            max_key_len = len(key)

    for i in range(1,max_key_len+1):
        keys = []
        for key in sol:
            if len(key) == i:
                keys.append(key)
        keys.sort()
        for key in keys:
            if sol[key] == 0: continue
            if sol[key] > 0:
                r += '+'
            else:
                r += '-'
            r += str(sol[key]) + key if sol[key] > 1 else key
    return r[1:] if r.startswith('+') else r
