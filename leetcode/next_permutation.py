"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""


class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        swap_index = None
        for i in range(len(nums)):
            if nums[i] < max(nums[i:]):
                swap_index = i

        if swap_index is None:
            nums.reverse()
            return

        for j in range(swap_index + 1, len(nums)):
            if nums[swap_index] < nums[j]:
                swap_to = j

        nums[swap_index], nums[swap_to] = nums[swap_to], nums[swap_index]

        # bubble sort remaining
        for k in range(swap_index + 1, len(nums) - 1):
            for l in range(swap_index + 1, len(nums) - 1):
                if nums[l] > nums[l + 1]:
                    t = nums[l + 1]
                    nums[l + 1] = nums[l]
                    nums[l] = t
        return
