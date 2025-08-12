# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/description/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # brute-force
        # TC: O(2^n), SC: O(n)
        n = len(prices)
        def dfs(i, currK, buy):
            if currK == 0:
                return 0
            if i == n:
                return 0
            if buy:
                return max(dfs(i + 1, currK, not buy) - prices[i], dfs(i + 1, currK, buy))
            else:
                return max(dfs(i + 1, currK - 1, not buy) + prices[i], dfs(i + 1, currK, buy))
        return dfs(0, 2, True)

        # optimal
        # TC: O(n^2), SC: O(n)
        n = len(prices)
        dp = {}    # (i, currK, buy) -> max profit from i to end
        def dfs(i, currK, buy):
            if currK == 0:
                return 0
            if i == n:
                return 0
            if (i, currK, buy) in dp:
                return dp[(i, currK, buy)]
            if buy:
                dp[(i, currK, buy)] = max(dfs(i + 1, currK, not buy) - prices[i], dfs(i + 1, currK, buy)) 
            else:
                dp[(i, currK, buy)] = max(dfs(i + 1, currK - 1, not buy) + prices[i], dfs(i + 1, currK, buy))
            return dp[(i, currK, buy)]
        return dfs(0, 2, True)