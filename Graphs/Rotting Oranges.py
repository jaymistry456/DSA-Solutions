# https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # TC: O(m*n), SC: O(m*n)
        m = len(grid)
        n = len(grid[0])
        EMPTY, FRESH, ROTTEN = 0, 1, 2
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]] # neighbor naviagtion
        # put all the rotten oranges in a queue
        q = deque()
        freshCount = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == ROTTEN:
                    q.append((r, c))
                elif grid[r][c] == FRESH:
                    freshCount += 1
        # start the bfs at once from all rotten oranges
        res = -1
        while q:
            res += 1
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    if 0 <= r + dr < m and 0 <= c + dc < n and grid[r + dr][c + dc] == FRESH:
                        grid[r + dr][c + dc] = ROTTEN
                        freshCount -= 1
                        q.append((r + dr, c + dc))
        if freshCount == 0:
            if res == -1:
                return 0
            else:
                return res
        else:
            return -1