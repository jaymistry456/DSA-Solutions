# https://leetcode.com/problems/distinct-subsequences/

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # brute-force
        # TC: O(2^n1), SC: O(n1+n2)
        n1 = len(s)
        n2 = len(t)
        def dfs(i, j):
            if j == n2:
                return 1
            if i == n1:
                return 0
            if s[i] == t[j]:
                return dfs(i + 1, j + 1) + dfs(i + 1, j)
            else:
                return dfs(i + 1, j)
        return dfs(0, 0)


        # optimal
        # TC: O(n1*n2), SC: O(n1*n2)
        n1 = len(s)
        n2 = len(t)
        dp = {}    # (i, j) -> no. of subsequences from (i, j) to the end
        def dfs(i, j):
            if j == n2:
                return 1
            if i == n1:
                return 0
            if (i, j) in dp:
                return dp[(i, j)]
            if s[i] == t[j]:
                dp[(i, j)] = dfs(i + 1, j + 1) + dfs(i + 1, j)
            else:
                dp[(i, j)] = dfs(i + 1, j)
            return dp[(i, j)]
        return dfs(0, 0)