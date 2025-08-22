# https://leetcode.com/problems/triangle/

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # brute-force
        # TC: O(2^n), SC: O(n)
        n = len(triangle)
        def dfs(i, j):
            if i == n:
                return 0
            return triangle[i][j] + min(dfs(i + 1, j), dfs(i + 1, j + 1))
        return dfs(0, 0)


        # optimal
        # TC: O(n^2), SC: O(n^2)
        dp = {}    # (i, j) -> minSum from (i, j)
        n = len(triangle)
        def dfs(i, j):
            if i == n:
                return 0
            if (i, j) in dp:
                return dp[(i, j)]
            dp[(i, j)] = triangle[i][j] + min(dfs(i + 1, j), dfs(i + 1, j + 1))
            return dp[(i, j)]
        return dfs(0, 0)