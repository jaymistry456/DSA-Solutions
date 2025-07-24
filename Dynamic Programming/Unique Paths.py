# https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # brute-force
        # TC: O(2^(m+n)), SC: O(m+n)
        def dfs(r, c):
            if r == m - 1 and c == n - 1:
                return 1
            if r == m or c == n:
                return 0
            return dfs(r, c + 1) + dfs(r + 1, c)
        return dfs(0, 0)


        # optimal
        # TC: O(m*n), SC: O(m*n)
        dp = {} # key ((r, c)) -> value (no. of paths to reach bottom)
        def dfs(r, c):
            if r == m - 1 and c == n - 1:
                return 1
            if r == m or c == n:
                return 0
            if (r, c) in dp:
                return dp[(r, c)]
            dp[(r, c)] = dfs(r, c + 1) + dfs(r + 1, c)
            return dp[(r, c)]
        return dfs(0, 0)