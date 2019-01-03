"""
Calculate the angle between hour hand and minute hand.

There can be two angles between hands, we need to print minimum of two. Also, we need to print floor of final result angle. For example, if the final angle is 10.61, we need to print 10.



Input:

The first line of input contains a single integer T denoting the number of test cases. Then T test cases follow. Each test case consists of one line conatining two space separated numbers h and m where h is hour and m is minute.

Output:
Coresponding to each test case, print the angle b/w hour and min hand in a separate line.

Constraints:

1 ≤ T ≤ 100
1 ≤ h ≤ 12
1 ≤ m ≤ 60

Example:

Input
2
9 60
3 30

Output
90
75
"""

from math import floor


def get_hand_seperation(hour, minute):
    hour_position = (hour + (minute / 60)) * 30
    minute_position = minute * 6

    return abs(hour_position - minute_position)


if __name__ == '__main__':

    t = int(input())

    for i in range(t):
        hour, minute = map(lambda x: float(x), input().split(' '))

        if minute == 60:
            minute = 0

        hand_seperation = get_hand_seperation(hour, minute)
        print(floor(min(hand_seperation, 360 - hand_seperation)))
