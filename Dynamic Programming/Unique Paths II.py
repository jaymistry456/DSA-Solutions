# https://leetcode.com/problems/unique-paths-ii/description/

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # brute-force
        # TC: O((m*n)^2), SC: O(m*n)
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        def dfs(i, j):
            if i >= m or j >= n or obstacleGrid[i][j] == 1:
                return 0
            if i == m - 1 and j == n - 1:
                return 1
            return dfs(i + 1, j) + dfs(i, j + 1)
        return dfs(0, 0)


        # optimal
        # TC: O(m*n), SC: O(m*n)
        dp = {}    # (i, j) -> no. of paths
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        def dfs(i, j):
            if i >= m or j >= n or obstacleGrid[i][j] == 1:
                return 0
            if i == m - 1 and j == n - 1:
                return 1
            if (i, j) in dp:
                return dp[(i, j)]
            dp[(i, j)] = dfs(i + 1, j) + dfs(i, j + 1)
            return dp[(i, j)]
        return dfs(0, 0)