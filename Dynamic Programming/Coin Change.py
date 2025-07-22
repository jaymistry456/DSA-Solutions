# https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # brute-force
        # TC: O(n^amount), SC: O(amount)
        def dfs(amount):
            if amount == 0:
                return 0
            res = sys.maxsize
            for coin in coins:
                if amount - coin >= 0:
                    res = min(res, 1 + dfs(amount - coin))
            return res
        res = dfs(amount)
        return res if res != sys.maxsize else -1


        # optimal
        # TC: O(n*amount), SC: O(amount)
        dp = {} # key (x) -> value (min no. of coins required to x)
        def dfs(amount):
            if amount == 0:
                return 0
            if amount in dp:
                return dp[amount]
            dp[amount] = sys.maxsize
            for coin in coins:
                if amount - coin >= 0:
                    dp[amount] = min(dp[amount], 1 + dfs(amount - coin))
            return dp[amount]
        res = dfs(amount)
        return res if res != sys.maxsize else -1