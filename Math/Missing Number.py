# https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # brute-force
        # TC: O(n^2), SC: O(1)
        for i in range(len(nums) + 1):
            if i not in nums:
                return i


        # better
        # TC: O(n), SC: O(n)
        hashset = set(nums)
        for i in range(len(nums) + 1):
            if i not in hashset:
                return i


        # optimal
        # TC: O(n), SC: O(1)
        res = 0
        for i in range(len(nums) + 1):
            res ^= i
        for i in range(len(nums)):
            res ^= nums[i]
        return res