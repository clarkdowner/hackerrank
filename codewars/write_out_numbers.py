"""
Create a function that transforms any positive number to a string representing the number in words. The function should
work for all numbers between 0 and 999999.
"""


def number2words(nm):
    """ works for numbers between 0 and 999999 """
    singles = {
        '0': '',
        '1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine',
    }

    teens = {
        '10': 'ten',
        '11': 'eleven',
        '12': 'twelve',
        '13': 'thirteen',
        '14': 'fourteen',
        '15': 'fifteen',
        '16': 'sixteen',
        '17': 'seventeen',
        '18': 'eighteen',
        '19': 'nineteen',
    }

    tens = {
        '2': 'twenty',
        '3': 'thirty',
        '4': 'forty',
        '5': 'fifty',
        '6': 'sixty',
        '7': 'seventy',
        '8': 'eighty',
        '9': 'ninety',
    }

    if nm == 0: return 'zero'

    def helper(n):
        m, num = len(n) - 1, ''
        for i in range(m,-1,-1):
            if i == m:
                num += singles[n[i]]
            elif i == m-1 and n[i] == '1':
                num = teens[n[i]+n[i+1]]
            elif i == m-1 and n[i] != '0':
                if len(num):
                    num = tens[n[i]] + '-' + num
                else:
                    num = tens[n[i]]
            elif i == m-2 and n[i] != '0':
                num = (singles[n[i]] + ' hundred ' + num).strip()
        return num

    nm = str(nm)
    if len(nm) > 3:
        return (helper(nm[:-3]) + ' thousand ' + helper(nm[-3:])).strip()
    return (helper(nm[-3:])).strip()

print(number2words(1340))