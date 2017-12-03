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
        # subsets = set()
        # for num in nums:
        #     for subset in subsets:
        #         subsets.add(subset + (num,))
        #     subsets.add((num,))
        # return subsets
        nums.sort()
        subsets = [[]]
        for num in nums:
            for subset in subsets[::]:
                subsets.append(subset[::] + [num])
            subsets.append([num])
        tups = [tuple(x) for x in subsets]
        sets = set(tups)
        return [list(x) for x in sets]

s = Solution()
print(s.subsetsWithDup([1,2,2]))
