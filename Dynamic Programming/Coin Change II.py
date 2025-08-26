# https://leetcode.com/problems/coin-change-ii/description/

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # brute-force
        # TC: O(2^amount), SC: O(amount)
        n = len(coins)
        def dfs(i, currSum):
            if currSum == amount:
                return 1
            if i == n or currSum > amount:
                return 0
            return dfs(i + 1, currSum) + dfs(i, currSum + coins[i])
        return dfs(0, 0)


        # optimal
        # TC: O(n*amount), SC: O(amount)
        n = len(coins)
        dp = {}    # (i, currSum) -> no. ways to form amount from (i, currSum)
        def dfs(i, currSum):
            if currSum == amount:
                return 1
            if i == n or currSum > amount:
                return 0
            if (i, currSum) in dp:
                return dp[(i, currSum)]
            dp[(i, currSum)] = dfs(i + 1, currSum) + dfs(i, currSum + coins[i])
            return dp[(i, currSum)]
        return dfs(0, 0)