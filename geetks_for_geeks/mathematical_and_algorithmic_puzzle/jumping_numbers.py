"""
Given a positive number X. Find all Jumping Numbers smaller than or equal to X.
Jumping Number: A number is called Jumping Number if all adjacent digits in it differ by only 1. All single digit numbers are considered as Jumping Numbers. For example 7, 8987 and 4343456 are Jumping numbers but 796 and 89098 are not.

Input:
The first line of the input contains T denoting the number of testcases. Each testcase contain a positive number X.

Output:
Output all the jumping numbers less than X in sorted order. Jump to example for better understanding.

Constraints:
1 <= T <= 100
1 <= N <= 109

Example:
Input:
2
10
50
Output:
0 1 2 3 4 5 6 7 8 9 10
0 1 2 3 4 5 6 7 8 9 10 12 21 23 32 34 43 45

Explanation:
Testcase 2: Here, the most significant digits of each jumping number is following increasing order, i.e., jumping numbers starting from 0, followed by 1, then 2 and so on, themselves being in increasing order 2, 21, 23.
"""


def get_jumpers(val):
    val_length = len(str(val))

    digits = list(range(1, 10))
    current_crop = [str(x) for x in digits]
    jumpers = ['0'] + current_crop

    for i in range(val_length - 1, 0, -1):
        next_crop = list()
        for num in current_crop:
            last_digit = int(num[-1])

            if last_digit > 0:
                dec = last_digit - 1
                next_crop.append(num + str(dec))
            if last_digit < 9:
                inc = last_digit + 1
                next_crop.append(num + str(inc))

        current_crop = next_crop
        jumpers.extend(current_crop)

    return list(filter(lambda x: int(x) < val, jumpers))


if __name__ == '__main__':

    test_cases = int(input())

    for i in range(test_cases):
        test_value = int(input())
        jumpers = get_jumpers(test_value)
        print(' '.join(jumpers))
