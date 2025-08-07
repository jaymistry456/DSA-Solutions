# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # TC: O(n), SC: O(1)
        pos = 0
        i = 0
        n = len(nums)
        while i < n:
            nums[pos] = nums[i]
            i += 1
            pos += 1
            if i < n and nums[i] == nums[i - 1]:
                nums[pos] = nums[i]
                i += 1
                pos += 1
                while i < n and nums[i] == nums[i - 1]:
                    i += 1
        return pos