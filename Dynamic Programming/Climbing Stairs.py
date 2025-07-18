# https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        # brute-force
        # TC: O(2^n), SC: O(n)
        def dfs(i):
            if i == n:
                return 1
            elif i > n:
                return 0
            return dfs(i + 1) + dfs(i + 2)
        return dfs(0)


        # optimal using top-down dp
        # TC: O(n), SC: O(n)
        dp = {} # key (step) -> val (number of ways to reach top from step)
        def dfs(i):
            if i == n:
                return 1
            elif i > n:
                return 0
            if i in dp:
                return dp[i]
            dp[i] = dfs(i + 1) + dfs(i + 2)
            return dp[i]
        return dfs(0)