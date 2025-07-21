# https://leetcode.com/problems/01-matrix/

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # TC: O(m*n), SC: O(m*n)
        m = len(mat)
        n = len(mat[0])
        res = [[0] * n for _ in range(m)]
        q = deque() # (r, c) pairs of 0s
        visited = set()
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        curr = 1
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    if 0 <= r + dr < m and 0 <= c + dc < n and (r + dr, c + dc) not in visited and mat[r + dr][c + dc] != 0:
                        res[r + dr][c + dc] = curr
                        q.append((r + dr, c + dc))
                        visited.add((r + dr, c + dc))
            curr += 1
        return res