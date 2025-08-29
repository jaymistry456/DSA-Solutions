# https://leetcode.com/problems/min-cost-climbing-stairs/

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # brute-force
        # TC: O(2^n), SC: O(n)
        n = len(cost)
        def dfs(i):
            if i >= n:
                return 0
            return cost[i] + min(dfs(i + 1), dfs(i + 2))
        return min(dfs(0), dfs(1))


        # optimal
        # TC: O(n^2), SC: O(n)
        n = len(cost)
        dp = {}    # i -> min cost to end from i to the end
        def dfs(i):
            if i >= n:
                return 0
            if i in dp:
                return dp[i]
            dp[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))
            return dp[i]
        return min(dfs(0), dfs(1))