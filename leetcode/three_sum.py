"""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""


class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # sols = set()
        # s_hash = {}
        # for i in range(len(nums) - 1):
        #     for j in range(i+1, len(nums)):
        #         key = nums[i] + nums[j]
        #         if key not in s_hash:
        #             s_hash[key] = set()
        #         s_hash[key].add((min(i, j), max(i, j),))
        # print(s_hash)
        # for i in range(len(nums)):
        #     key = -1 * nums[i]
        #     if key in s_hash:
        #         print('key is: ', key)
        #         for x in s_hash[nums[i]]:
        #             print('hashes: ', nums[x[0]], nums[x[1]])
        #             if i not in x:
        #                 sol = tuple(sorted([nums[x[0]], nums[x[1]], nums[i]]))
        #                 sols.add(sol)
        #
        # return [list(x) for x in sols]
        solutions = set()
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        vals = [nums[i], nums[j], nums[k]]
                        vals.sort()
                        solutions.add(tuple(vals))
        return [list(x) for x in solutions]

s = Solution()
# print(s.threeSum([-1, 0, -1]))
print(s.threeSum([-1, 0, 1, 2, -1, -4]))
