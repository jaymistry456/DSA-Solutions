# https://www.geeksforgeeks.org/problems/steps-by-knight5927/1

from collections import deque

class Solution:
    def minStepToReachTarget(self, knightPos, targetPos, n):
        # TC: O(n^2), SC: O(n^2)
        directions = [[2, 1], [-2, 1], [2, -1], [-2, -1], [1, 2], [-1, 2], [1, -2], [-1, -2]]
        q = deque()
        q.append((knightPos[0], knightPos[1]))
        visited = set()
        visited.add((knightPos[0], knightPos[1]))
        res = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                if r == targetPos[0] and c == targetPos[1]:
                    return res
                for dr, dc in directions:
                    if (r + dr, c + dc) not in visited:
                        visited.add((r + dr, c + dc))
                        q.append((r + dr, c + dc))
            res += 1