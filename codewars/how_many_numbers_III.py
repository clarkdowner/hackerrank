"""
We want to generate all the numbers of three digits that:

the value of adding their corresponding ones(digits) is equal to 10.

their digits are in increasing order (the numbers may have two or more equal contiguous digits)

The numbers that fulfill the two above constraints are: 118, 127, 136, 145, 226, 235, 244, 334

Make a function that receives two arguments:

the sum of digits value

the amount of desired digits for the numbers

The function should output an array with three values: [1,2,3]

1 - the total amount of all these possible numbers

2 - the minimum number

3 - the maximum numberwith

The example given above should be:

find_all(10, 3) == [8, 118, 334]
If we have only one possible number as a solution, it should output a result like the one below:

find_all(27, 3) == [1, 999, 999]
If there are no possible numbers, the function should output the empty array.

find_all(84, 4) == []
The number of solutions climbs up when the number of digits increases.

find_all(35, 6) == [123, 116999, 566666]
Features of the random tests:

Numbers of tests: 111
Sum of digits value between 20 and 65
Amount of digits between 2 and 15
"""


def find_all(sum_dig, digs):
    nums = []
    if sum_dig < 1 or sum_dig > digs * 9:
        return nums

    i = int('1'*digs)
    while i <= (10**digs) - 1:
        if is_sol(sum_dig, i):
            nums.append(i)
        i = find_next(i)

    return nums if not len(nums) else [len(nums), nums[0], nums[-1]]


def is_sol(sum_dig, num):
    return sum_dig == sum([int(x) for x in str(num)])


def find_next(num):
    digs = [int(x) for x in str(num + 1)]
    if 0 in digs:
        ind = digs.index(0)
        digs = digs[:ind] + [digs[ind-1]] * (len(digs)-ind)
    return int(''.join([str(x) for x in digs]))
