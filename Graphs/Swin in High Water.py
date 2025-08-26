# https://leetcode.com/problems/swim-in-rising-water/description/

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # TC: O(n^2*logn), SC: O(n^2)
        minHeap = []    # (currT, r, c)
        heapq.heappush(minHeap, (grid[0][0], 0, 0))
        visited = set()
        visited.add((0, 0))
        m = len(grid)
        n = len(grid[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        while minHeap:
            currT, r, c = heapq.heappop(minHeap)
            if r == m - 1 and c == n - 1:
                return currT
            for dr, dc in directions:
                if 0 <= r + dr < m and 0 <= c + dc < n and (r + dr, c + dc) not in visited:
                    heapq.heappush(minHeap, (max(currT, grid[r + dr][c + dc]), r + dr, c + dc))
                    visited.add((r + dr, c + dc))