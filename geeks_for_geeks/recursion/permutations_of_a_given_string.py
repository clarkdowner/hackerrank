"""
Given a string, print all permutations of a given string.

Input:
The first line of input contains an integer T, denoting the number of test cases. Each test case contains a single string S in capital letter.

Output:
For each test case, print all permutations of a given string S with single space and all permutations should be in lexicographically increasing order.

Example:
Input:
2
ABC
ABSG

Output:
ABC ACB BAC BCA CAB CBA
ABGS ABSG AGBS AGSB ASBG ASGB BAGS BASG BGAS BGSA BSAG BSGA GABS GASB GBAS GBSA GSAB GSBA SABG SAGB SBAG SBGA SGAB SGBA
"""


def get_perms(remaining_string, existing_string=''):
    if len(remaining_string) == 0:
        return [existing_string]

    perms = list()
    for index, letter in enumerate(remaining_string):
        next_existing = existing_string + letter
        next_remaining = remaining_string[:index] + remaining_string[index + 1:]

        perms.extend(get_perms(next_remaining, next_existing))

    return perms


if __name__ == '__main__':

    test_cases = int(input())

    for _ in range(test_cases):
        string = input()
        perms = get_perms(string)
        # print(*sorted(perms))
