"""
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        subsets = [[]]
        for num in nums:
            for subset in subsets[::]:
                subsets.append(subset[::] + [num])
            subsets.append([num])
        sort = [sorted(x) for x in subsets]
        tups = [tuple(x) for x in sort]
        sets = set(tups)
        return [list(x) for x in sets]
