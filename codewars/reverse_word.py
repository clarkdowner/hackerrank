"""
Write a reverseWords function that accepts a string a parameter, and reverses each word in the string. Any spaces in the
string should be retained.
"""


def reverse_words(str):
    return ' '.join([x[::-1] for x in str.split(' ')])
