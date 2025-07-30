# https://leetcode.com/problems/decode-ways/description/

class Solution:
    def numDecodings(self, s: str) -> int:
        # brute-force
        # TC: O(2^n), SC: O(n)
        n = len(s)
        def dfs(i):
            if i == n:
                return 1
            if s[i] == '0':
                return 0
            if i + 1 < n and 1 <= int(s[i:i+2]) <= 26:
                return dfs(i + 1) + dfs(i + 2)
            else:
                return dfs(i + 1)
        return dfs(0)


        # optimal
        # TC: O(n), SC: O(n)
        dp = {} # key (i) -> value (no. of ways to decode)
        n = len(s)
        def dfs(i):
            if i == n:
                return 1
            if s[i] == '0':
                return 0
            if i in dp:
                return dp[i]
            if i + 1 < n and 1 <= int(s[i:i+2]) <= 26:
                dp[i] = dfs(i + 1) + dfs(i + 2)
            else:
                dp[i] = dfs(i + 1)
            return dp[i]
        return dfs(0)