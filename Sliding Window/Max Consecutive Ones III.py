# https://leetcode.com/problems/max-consecutive-ones-iii/description/

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # brute-force
        # TC: O(n^2), SC: O(1)
        n = len(nums)
        res = 0
        for i in range(n):
            currZeros = 0
            for j in range(i, n):
                if nums[j] == 0:
                    currZeros += 1
                if currZeros > k:
                    break
                res = max(res, j - i + 1)
        return res


        # optimal
        # TC: O(n), SC: O(1)
        n = len(nums)
        currZeros = 0
        res = 0
        l = 0
        r = 0
        while r < n:
            if nums[r] == 0:
                currZeros += 1
            while currZeros > k:
                if nums[l] == 0:
                    currZeros -= 1
                l += 1
            res = max(res, r - l + 1)
            r += 1
        return res