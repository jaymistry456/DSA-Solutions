# https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # brute-force
        # TC: O(n^2), SC: O(n)
        n = len(nums)
        hashset = set(nums)
        res = 0
        for i in range(n):
            curr = nums[i]
            length = 1
            while curr + length in hashset:
                length += 1
            res = max(res, length)
        return res


        # optimal
        # TC: O(n), SC: O(n)
        n = len(nums)
        hashset = set(nums)
        res = 0
        for num in hashset:
            if num - 1 in hashset:
                continue
            length = 1
            while num + length in hashset:
                length += 1
            res = max(res, length)
        return res