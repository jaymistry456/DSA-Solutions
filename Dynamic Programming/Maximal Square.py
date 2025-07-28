# https://leetcode.com/problems/maximal-square/description/

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # brute-force
        # TC: O((m*n)^2), SC: O(1)
        # Try all possible square sizes from each cell


        # optimal
        # TC: O(m*n), SC: O(m*n)
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        maxSide = 0
        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if matrix[r][c] == '1':
                    dp[r][c] = 1 + min(dp[r][c + 1], dp[r + 1][c + 1], dp[r + 1][c])
                    maxSide = max(maxSide, dp[r][c])
        return maxSide * maxSide