# https://leetcode.com/problems/number-of-islands/description/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # DFS
        # TC: O(m*n), SC: O(m*n)
        m = len(grid)
        n = len(grid[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]] # neighbor navigation
        visited = set() # (r, c) which have been visited
        def dfs(r, c):
            visited.add((r, c))
            for dr, dc in directions:
                if 0 <= r + dr < m and 0 <= c + dc < n and (r + dr, c + dc) not in visited and grid[r + dr][c + dc] == '1':
                    dfs(r + dr, c + dc)
        res = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1' and (r, c) not in visited:
                    dfs(r, c)
                    res += 1
        return res


        # BFS
        # TC: O(m*n), SC: O(m*n)
        m = len(grid)
        n = len(grid[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]] # neighbor navigation
        visited = set() # (r, c) which have been visited
        def bfs(r, c):
            visited.add((r, c))
            q = deque()
            q.append((r, c))
            while q:
                currRow, currCol = q.popleft()
                for dr, dc in directions:
                    if 0 <= currRow + dr < m and 0 <= currCol + dc < n and (currRow + dr, currCol + dc) not in visited and grid[currRow + dr][currCol + dc] == '1':
                        q.append((currRow + dr, currCol + dc))
                        visited.add((currRow + dr, currCol + dc))
        res = 0 
        for r in range(m):
            for c in range(n):
                if (r, c) not in visited and grid[r][c] == '1':
                    bfs(r, c)
                    res += 1
        return res