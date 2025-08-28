# https://leetcode.com/problems/surrounded-regions/

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # DFS
        # TC: O(m*n), SC: O(m*n)
        m = len(board)
        n = len(board[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        def dfs(r, c):
            board[r][c] = "T"
            for dr, dc in directions:
                if 0 <= r + dr < m and 0 <= c + dc < n and board[r + dr][c + dc] == "O":
                    board[r + dr][c + dc] = "T"
                    dfs(r + dr, c + dc)
        for r in range(m):
            if board[r][0] == "O":
                dfs(r, 0)
            if board[r][n - 1] == "O":
                dfs(r, n - 1)
        for c in range(n):
            if board[0][c] == "O":
                dfs(0, c)
            if board[m - 1][c] == "O":
                dfs(m - 1, c)
        for r in range(m):
            for c in range(n):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"



        # BFS
        # TC: O(m*n), SC: O(m*n)
        m = len(board)
        n = len(board[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        def bfs(r, c):
            board[r][c] = "T"
            q = deque()
            q.append((r, c))
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    if 0 <= r + dr < m and 0 <= c + dc < n and board[r + dr][c + dc] == "O":
                        board[r + dr][c + dc] = "T"
                        q.append((r + dr, c + dc))
        for r in range(m):
            if board[r][0] == "O":
                bfs(r, 0)
            if board[r][n - 1] == "O":
                bfs(r, n - 1)
        for c in range(n):
            if board[0][c] == "O":
                bfs(0, c)
            if board[m - 1][c] == "O":
                bfs(m - 1, c)
        for r in range(m):
            for c in range(n):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"