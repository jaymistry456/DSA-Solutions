# https://leetcode.com/problems/move-zeroes/description/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # TC: O(n), SC: O(1)
        pos = 0
        i = 0
        n = len(nums)
        while i < n:
            while i < n and nums[i] == 0:
                i += 1
            if i < n:
                nums[pos] = nums[i]
                pos += 1
                i += 1
        while pos < n:
            nums[pos] = 0
            pos += 1