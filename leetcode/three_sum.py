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
        sols = set()
        nums.sort()
        for i in range(len(nums) - 2):
            if nums[i] <= 0 and (nums[i] != nums[i - 1] or i == 0):
                j = i + 1
                if nums[i] + nums[j] <= 0:
                    k = len(nums) - 1
                    while j != k:
                        sum = nums[i] + nums[j] + nums[k]
                        if sum == 0:
                            sol = (nums[i], nums[j], nums[k])
                            sols.add(sol)
                            j += 1
                        elif sum < 0:
                            j += 1
                        else:
                            k -= 1
                else:
                    continue

        return [list(x) for x in sols]


# s = Solution()
# print(s.threeSum([-1, 0, 1, 2, -1, -4]))
