"""
Given a sorted array, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra
memory.

Example:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the new length.
"""


class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)

        last_seen = nums[0]
        i = 1
        while i < len(nums):
            if nums[i] == last_seen:
                nums.pop(i)
            else:
                last_seen = nums[i]
                i += 1
        if len(nums) > 1 and nums[-2] == nums[-1]:
            nums.pop(-1)
        return len(nums)

s = Solution()
print(s.removeDuplicates([1, 2, 2]))
