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
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longest = ''
        for i in range(len(s)):
            temp = self.helper(s, i, i)
            if len(temp) > len(longest):
                longest = temp
            temp = self.helper(s, i, i + 1)
            if len(temp) > len(longest):
                longest = temp
        return longest

    def helper(self, s, l, r):
        pal = ''
        while l >= 0 and r < len(s) and s[l] == s[r]:
            pal = s[l:r+1]
            l -= 1
            r += 1
        return pal

s = Solution()
print(s.longestPalindrome('babad'))
print(s.longestPalindrome('babaddtattarrattatddetartrateedredividerb'))
print(s.longestPalindrome('cbbd'))
