"""
https://stackoverflow.com/questions/54336337/position-of-tuple-element-in-the-list

I have list of tuples:

tuple_list = [(a, b), (c, d), (e, f), (g, h)]
How to get position of second element in tuple in second position of the list for example.

I need it because i want to change this list the way that every second element of tuple equals to first element from next tuple. Like this:

tuple_list = [(a, c), (c, e), (e, g), (g, h)]
"""

a, b, c, d, e, f, g, h = 0, 1, 2, 3, 4, 5, 6, 7  # examples
tuple_list = [(a, b), (c, d), (e, f), (g, h)]

for i in range(len(tuple_list)-1):
    new_tuple = (tuple_list[i][0], tuple_list[i+1][0])
    tuple_list[i] = new_tuple
