# https://leetcode.com/problems/pacific-atlantic-water-flow/description/

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # brute-force
        # TC: O(4^(m*n)*m*n), SC: O(m*n)
        m = len(heights)
        n = len(heights[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]] # neighbor navigation
        pacific = False
        atlantic = False
        def dfs(r, c, prev):
            nonlocal pacific, atlantic
            if r < 0 or c < 0:
                pacific = True
                return
            if r >= m or c >= n:
                atlantic = True
                return
            if heights[r][c] > prev:
                return
            temp = heights[r][c]
            heights[r][c] = sys.maxsize
            for dr, dc in directions:
                dfs(r + dr, c + dc, temp)
                if pacific and atlantic:
                    break
            heights[r][c] = temp

        res = []
        for r in range(m):
            for c in range(n):
                dfs(r, c, sys.maxsize)
                if pacific and atlantic:
                    res.append([r, c])
                pacific = False
                atlantic = False
        return res


        # optimal (DFS)
        # TC: O(m*n), SC: O(m*n)
        m = len(heights)
        n = len(heights[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        pacific = set()
        atlantic = set()
        def dfs(r, c, visited, prev):
            visited.add((r, c))
            for dr, dc in directions:
                if 0 <= r + dr < m and 0 <= c + dc < n and (r + dr, c + dc) not in visited and heights[r + dr][c + dc] >= heights[r][c]:
                    dfs(r + dr, c + dc, visited, heights[r + dr][c + dc])
        for r in range(m):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, n - 1, atlantic, heights[r][n - 1])
        for c in range(n):
            dfs(0, c, pacific, heights[0][c])
            dfs(m - 1, c, atlantic, heights[m - 1][c])
        res = pacific.intersection(atlantic)
        return list(res)


        # optimal (BFS)
        # TC: O(m*n), SC: O(m*n)
        m = len(heights)
        n = len(heights[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        pacific = set()
        atlantic = set()
        def bfs(r, c, visited):
            visited.add((r, c))
            q = deque()
            q.append((r, c))
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    if 0 <= r + dr < m and 0 <= c + dc < n and (r + dr, c + dc) not in visited and heights[r + dr][c + dc] >= heights[r][c]:
                        q.append((r + dr, c + dc))
                        visited.add((r + dr, c + dc))
        for r in range(m):
            bfs(r, 0, pacific)
            bfs(r, n - 1, atlantic)
        for c in range(n):
            bfs(0, c, pacific)
            bfs(m - 1, c, atlantic)
        res = pacific.intersection(atlantic)
        return list(res)