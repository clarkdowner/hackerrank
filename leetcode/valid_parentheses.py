"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
"""


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for p in s:
            if p == '(' or p == '{' or p == '[':
                stack.append(p)
            elif not len(stack) or \
                        (p == ')' and stack[len(stack) - 1] != '(') or \
                        (p == '}' and stack[len(stack) - 1] != '{') or \
                        (p == ']' and stack[len(stack) - 1] != '['):
                return False
            else:
                stack.pop()
        if len(stack):
            return False
        return True
