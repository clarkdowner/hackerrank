"""
Given a keypad as shown in diagram, and an N digit number. List all words which are possible by pressing these numbers.



Input:
The first line of input contains an integer T denoting the number of test cases. T testcases follow. Each testcase contains two lines of input. The first line of each test case is N, N is the number of digits. The second line of each test case contains D[i], N number of digits.

Output:
Print all possible words from phone digits with single space.

Constraints:
1 <= T <= 10
1 <= N <= 10
2 <=  D[i] <= 9

Example:
Input:
1
3
2 3 4

Output:
adg adh adi aeg aeh aei afg afh afi bdg bdh bdi beg beh bei bfg bfh bfi cdg cdh cdi ceg ceh cei cfg cfh cfi
"""

DIAL_MAP = {
    1: '',
    2: 'abc',
    3: 'def',
    4: 'ghi',
    5: 'jkl',
    6: 'mno',
    7: 'pqrs',
    8: 'tuv',
    9: 'wxyz',
    0: '',
}


def get_dial_words(digits, word=''):
    if len(digits) == 0:
        return [word]

    words = list()

    for letter in DIAL_MAP[digits[0]]:
        words.extend(get_dial_words(digits[1:], word + letter))

    return words


if __name__ == '__main__':

    test_cases = int(input())

    for _ in range(test_cases):
        n = int(input())
        digits = list(map(int, input().split()))
        # print(*sorted(get_dial_words(digits)))
