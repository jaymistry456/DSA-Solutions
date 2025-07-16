# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # brute-force
        # TC: O(n^2), SC: O(1)
        res = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                res = max(res, prices[j] - prices[i])
        return res

        # optimal
        # TC: O(n), SC: O(1)
        minBuy = prices[0]
        res = 0
        for i in range(1, len(prices)):
            res = max(res, prices[i] - minBuy)
            minBuy = min(minBuy, prices[i])
        return res