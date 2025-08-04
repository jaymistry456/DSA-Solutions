# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/description/

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # brute-force
        # TC: O((m*n)^2), SC: O(m*n)
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        m = len(matrix)
        n = len(matrix[0])
        def dfs(r, c):
            curr = 0
            for dr, dc in directions:
                if 0 <= r + dr < m and 0 <= c + dc < n and matrix[r + dr][c + dc] > matrix[r][c]:
                    curr = max(curr, dfs(r + dr, c + dc))
            return 1 + curr
        res = 1
        for r in range(m):
            for c in range(n):
                res = max(res, dfs(r, c))
        return res


        # optimal
        # TC: O(m*n), SC: O(m*n)
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        m = len(matrix)
        n = len(matrix[0])
        dp = {} # key (r, c) -> val (maximum path from (r, c))
        def dfs(r, c):
            if (r, c) in dp:
                return dp[(r, c)]
            curr = 0
            for dr, dc in directions:
                if 0 <= r + dr < m and 0 <= c + dc < n and matrix[r + dr][c + dc] > matrix[r][c]:
                    curr = max(curr, dfs(r + dr, c + dc))
            dp[(r, c)] = 1 + curr
            return dp[(r, c)]
        res = 1
        for r in range(m):
            for c in range(n):
                res = max(res, dfs(r, c))
        return res