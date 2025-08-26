# https://neetcode.io/problems/islands-and-treasure

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # TC: O(m*n), SC: O(m*n)
        INF = 2147483647
        WATER = -1
        TREASURE = 0
        q = deque()    # (r, c) of TREASURES
        m = len(grid)
        n = len(grid[0])
        for r in range(m):
            for c in range(n):
                if grid[r][c] == TREASURE:
                    q.append((r, c))
        currDist = 1
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    if 0 <= r + dr < m and 0 <= c + dc < n and grid[r + dr][c + dc] == INF:
                        grid[r + dr][c + dc] = currDist
                        q.append((r + dr, c + dc))
            currDist += 1