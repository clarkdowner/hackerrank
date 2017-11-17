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
        sols = []
        s_hash = {}
        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):
                key = nums[i] + nums[j]
                if key not in s_hash:
                    s_hash[key] = []
                s_hash[key].append((i, j))
        print(s_hash)
        for i in range(len(nums)):
            key = -1 * nums[i]
            print(key)
            if key in s_hash:
                for x in s_hash[nums[i]]:
                    if i not in x:
                        sol = [nums[x[0]], nums[x[1]], nums[i]]
                        sols.append(sol)

        return sols

s = Solution()
print(s.threeSum([-1, 0, 1, 2, -1, -4]))
