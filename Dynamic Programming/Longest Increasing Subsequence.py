# https://leetcode.com/problems/longest-increasing-subsequence/description/

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # brute-force
        # TC: O(2^n), SC: O(n)
        n = len(nums)
        def backtrack(prev, new):
            if new == n:
                return 0
            # skip
            res = backtrack(prev, new + 1)
            # include
            if prev == -1 or nums[prev] < nums[new]:
                res = max(res, 1 + backtrack(new, new + 1))
            return res
        return backtrack(-1, 0)


        # optimal (top-down)
        # TC: O(n^2), SC: O(n^2)
        n = len(nums)
        dp = {} # key ((prev, new)) -> value (longest increasing subsequence from new)
        def backtrack(prev, new):
            if new == n:
                return 0
            if (prev, new) in dp:
                return dp[(prev, new)]
            # skip
            dp[(prev, new)] = backtrack(prev, new + 1)
            # include
            if prev == -1 or nums[prev] < nums[new]:
                dp[(prev, new)] = max(dp[(prev, new)], 1 + backtrack(new, new + 1))
            return dp[(prev, new)]
        return backtrack(-1, 0)


        # optimal (bottom-up)
        # TC: O(n^2), SC: O(n)
        n = len(nums)
        dp = [1] * n
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)