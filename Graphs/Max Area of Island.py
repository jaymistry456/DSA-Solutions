# https://leetcode.com/problems/max-area-of-island/description/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # DFS
        # TC: O(m*n), SC: O(m*n)
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        m = len(grid)
        n = len(grid[0])
        visited = set()
        def dfs(r, c):
            curr = 1
            for dr, dc in directions:
                if 0 <= r + dr < m and 0 <= c + dc < n and (r + dr, c + dc) not in visited and grid[r + dr][c + dc] == 1:
                    visited.add((r + dr, c + dc))
                    curr += dfs(r + dr, c + dc)
            return curr
        res = 0
        for r in range(m):
            for c in range(n):
                if (r, c) not in visited and grid[r][c] == 1:
                    visited.add((r, c))
                    res = max(res, dfs(r, c))
        return res


        # BFS
        # TC: O(m*n), SC: O(m*n)
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        m = len(grid)
        n = len(grid[0])
        visited = set()
        def bfs(r, c):
            curr = 1
            q = deque()
            q.append((r, c))
            visited.add((r, c))
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    if 0 <= r + dr < m and 0 <= c + dc < n and (r + dr, c + dc) not in visited and grid[r + dr][c + dc] == 1:
                        visited.add((r + dr, c + dc))
                        q.append((r + dr, c + dc))
                        curr += 1
            return curr
        res = 0
        for r in range(m):
            for c in range(n):
                if (r, c) not in visited and grid[r][c] == 1:
                    res = max(res, bfs(r, c))
        return res