# https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        # brute-force
        # TC: O(2^n), SC: O(n)
        n = len(nums)
        def dfs(i):
            if i >= n:
                return 0
            return max(dfs(i + 1), nums[i] + dfs(i + 2))
        return dfs(0)


        # optimal
        # TC: O(n), SC: O(n)
        n = len(nums)
        dp = {} # key (i) -> value (max profit from this index to the end)
        def dfs(i):
            if i >= n:
                return 0
            if i in dp:
                return dp[i]
            dp[i] = max(dfs(i + 1), nums[i] + dfs(i + 2))
            return dp[i]
        return dfs(0)