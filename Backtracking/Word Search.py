# https://leetcode.com/problems/word-search/description/

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # DFS
        # TC: O(4^L*(m*n)), SC: O(L)
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]] # neighbor navigation
        m = len(board)
        n = len(board[0])
        visited = set() # (r, c) which have been visited
        def dfs(r, c, i):
            if board[r][c] != word[i]:
                return False
            else:
                if i == len(word) - 1:
                    return True
                visited.add((r, c))
                for dr, dc in directions:
                    if 0 <= r + dr < m and 0 <= c + dc < n and (r + dr, c + dc) not in visited:
                        if dfs(r + dr, c + dc, i + 1):
                            return True
                visited.remove((r, c))
                return False
        for r in range(m):
            for c in range(n):
                if dfs(r, c, 0):
                    return True
        return False