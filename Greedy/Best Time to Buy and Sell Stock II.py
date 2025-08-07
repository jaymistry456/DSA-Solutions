# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # brute-force
        # TC: O(2^n), SC: O(n)
        n = len(prices)
        res = 0
        def dfs(i, buy):
            if i == n:
                return 0
            currProfit = 0
            if buy:
                # don't buy
                currProfit = max(currProfit, dfs(i + 1, buy))
                # buy
                currProfit = max(currProfit, dfs(i + 1, not buy) - prices[i])
            else:
                # don't sell
                currProfit = max(currProfit, dfs(i + 1, buy))
                # sell
                currProfit = max(currProfit, dfs(i + 1, not buy) + prices[i])
            return currProfit
        return dfs(0, True)


        # better
        # TC: O(n), SC: O(n)
        n = len(prices)
        dp = {}    # (i, buy) -> max profit from i till end
        def dfs(i, buy):
            if i == n:
                return 0
            if (i, buy) in dp:
                return dp[(i, buy)]
            dp[(i, buy)] = 0
            if buy:
                dp[(i, buy)] = max(dp[i, buy], dfs(i + 1, buy))    # skip
                dp[(i, buy)] = max(dp[i, buy], dfs(i + 1, not buy) - prices[i])    # buy
            else:
                dp[(i, buy)] = max(dp[i, buy], dfs(i + 1, buy))    # skip
                dp[(i, buy)] = max(dp[i, buy], dfs(i + 1, not buy) + prices[i])    # sell
            return dp[(i, buy)]
        return dfs(0, True)


        # optimal
        # TC: O(n), SC: O(1)
        n = len(prices)
        i = 0
        res = 0
        while i < n:
            buy = prices[i]
            i += 1
            while i < n and prices[i] <= prices[i - 1]:
                buy = prices[i]
                i += 1
            if i < n:
                sell = prices[i]
                while i < n and prices[i] >= prices[i - 1]:
                    sell = prices[i]
                    i += 1
                res += sell - buy
        return res