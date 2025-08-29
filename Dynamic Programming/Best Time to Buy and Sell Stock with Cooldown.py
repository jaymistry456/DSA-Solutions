# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # brute-force
        # TC: O(2^n), SC: O(n)
        n = len(prices)
        def dfs(i, buy):
            if i >= n:
                return 0
            if buy:
                return max(dfs(i + 1, False) - prices[i], dfs(i + 1, True))
            else:
                return max(dfs(i + 2, True) + prices[i], dfs(i + 1, False))
        return dfs(0, True)
            
        
        # optimal
        # TC: O(n^2), SC: O(n^2)
        n = len(prices)
        dp = {}    # (i, buy) -> max profit from i to the end
        def dfs(i, buy):
            if i >= n:
                return 0
            if (i, buy) in dp:
                return dp[(i, buy)]
            if buy:
                dp[(i, buy)] = max(dfs(i + 1, False) - prices[i], dfs(i + 1, True))
            else:
                dp[(i, buy)] = max(dfs(i + 2, True) + prices[i], dfs(i + 1, False))
            return dp[(i, buy)]
        return dfs(0, True)