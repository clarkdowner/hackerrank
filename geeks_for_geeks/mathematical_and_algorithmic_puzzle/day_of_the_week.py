"""
Write a program that calculates the day of the week for any particular date in the past or future.

Input:

The first line of input contains a single integer T denoting the number of test cases. Then T test cases follow. Each test case consist of one line. The first line of each test case consists of an integer d,m and y, d is day, m is month and y is the year.

Output:

Print day of given date.

Constraints:

1 ≤ T ≤ 100
1990 ≤ Y ≤ 2100

Example:

Input:

2

28 12 1995

30 8 2010

Output

Thursday

Monday
"""

import datetime


WEEKDAYS = {
    0: 'Monday',
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thursday',
    4: 'Friday',
    5: 'Saturday',
    6: 'Sunday',
}


def extract_weekday(string):
    day, month, year = [int(x) for x in string.split(' ')]
    date = datetime.datetime(year, month, day)

    return WEEKDAYS[date.weekday()]


if __name__ == '__main__':

    test_cases = int(input())

    for i in range(test_cases):
        print(extract_weekday(input()))
