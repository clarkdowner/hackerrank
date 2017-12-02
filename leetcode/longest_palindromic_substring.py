"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:

Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.
Example:

Input: "cbbd"

Output: "bb"
"""

class Solution(object):
    def longestPalindrome(self, s, l = 0, r = None):
        """
        :type s: str
        :rtype: str
        """
        if not len(s):
            return None

        if r is None:
            r = len(s)

        if l == r:
            return s[l:r]

        if s[l:r] == s[l:r][::-1]:
            return s[l:r]

        a = self.longestPalindrome(s, l + 1, r)
        b = self.longestPalindrome(s, l, r - 1)

        if len(a) > len(b):
            return a
        else:
            return b
