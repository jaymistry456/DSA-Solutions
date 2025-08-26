# https://leetcode.com/problems/min-cost-to-connect-all-points/

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # TC: O(n^2*logn), SC: O(n^2)
        n = len(points)
        minHeap = []    # (dist, nei)
        heapq.heappush(minHeap, (0, 0))
        res = 0
        visited = set()
        while len(visited) != n:
            currDist, currNode = heapq.heappop(minHeap)
            if currNode not in visited:
                res += currDist
                visited.add(currNode)
                for nei in range(n):
                    if nei not in visited:
                        neiX, neiY = points[nei]
                        currX, currY = points[currNode]
                        neiDist = abs(neiX - currX) + abs(neiY - currY)
                        heapq.heappush(minHeap, (neiDist, nei))
        return res