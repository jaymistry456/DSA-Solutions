# https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks/

class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        # TC: O(nlogn), SC: O(n)
        minHeap = []    # min diffs (capacity[i] - rocks[i])
        n = len(capacity)
        res = 0
        for i in range(n):
            currDiff = capacity[i] - rocks[i]
            if currDiff > 0:
                heapq.heappush(minHeap, currDiff)
            else:
                res += 1
        while minHeap and additionalRocks > 0:
            currDiff = heapq.heappop(minHeap)
            if currDiff <= additionalRocks:
                res += 1
                additionalRocks -= currDiff
        return res