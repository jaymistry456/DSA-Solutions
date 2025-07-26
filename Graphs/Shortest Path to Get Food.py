# https://leetcode.com/problems/shortest-path-to-get-food

class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        # brute-force
        # TC: O(4^m*n), SC: O(m*n)
        m = len(grid)
        n = len(grid[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        start = [0, 0]
        for r in range(m):
            for c in range(n):
                if grid[r][c] == '*':
                    start = [r, c]
        visited = set()
        def dfs(r, c, steps):
            if grid[r][c] == '#':
                return steps
            visited.add((r, c))
            res = sys.maxsize
            for dr, dc in directions:
                if 0 <= r + dr < m and 0 <= c + dc < n and (r + dr, c + dc) not in visited and grid[r + dr][c + dc] != 'X':
                    res = min(res, 1 + dfs(r + dr, c + dc))
            visited.remove((r, c))
            return res
        res = dfs(start[0], start[1], 0)
        if res == sys.maxsize:
            return -1
        else:
            return res


        # optimal
        # TC: O(m*n), SC: O(m*n)
        m = len(grid)
        n = len(grid[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        q = deque()
        visited = set()
        for r in range(m):
            for c in range(n):
                if grid[r][c] == '*':
                    q.append((r, c, 0))
                    visited.add((r, c))
                    break
            if q:
                break
        while q:
            r, c, dist = q.popleft()
            if grid[r][c] == '#':
                return dist
            for dr, dc in directions:
                if 0 <= r + dr < m and 0 <= c + dc < n and (r + dr, c + dc) not in visited and grid[r + dr][c + dc] != 'X':
                    q.append((r + dr, c + dc, dist + 1))
                    visited.add((r + dr, c + dc))
        return -1