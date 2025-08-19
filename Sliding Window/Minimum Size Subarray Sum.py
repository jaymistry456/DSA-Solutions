# https://leetcode.com/problems/minimum-size-subarray-sum/description/

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # brute-force
        # TC: O(n^2), SC: O(1)
        n = len(nums)
        res = float("inf")
        for i in range(n):
            currSum = 0
            for j in range(i, n):
                currSum += nums[j]
                if currSum >= target:
                    res = min(res, j - i + 1)
        return res if res != float("inf") else 0


        # optimal
        # TC: O(n), SC: O(1)
        n = len(nums)
        l = 0
        r = 0
        currSum = 0
        res = float("inf")
        while r < n:
            currSum += nums[r]
            while l <= r and currSum >= target:
                res = min(res, r - l + 1)
                currSum -= nums[l]
                l += 1
            r += 1
        return res if res != float("inf") else 0