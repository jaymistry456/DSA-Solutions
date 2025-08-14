# https://leetcode.com/problems/ipo/description/

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # brute-force
        # TC: O(n^2), SC: O(n)
        n = len(profits)
        hashset = set()
        for _ in range(k):
            maxProfit = 0
            currIndex = -1
            for i in range(n):
                if i not in hashset and capital[i] <= w and profits[i] > maxProfit:
                    currIndex = i
                    maxProfit = profits[i]
            if currIndex == -1:
                break
            w += maxProfit
            hashset.add(currIndex)
        return w


        # optimal
        # TC: O(nlogn), SC: O(n)
        n = len(profits)
        minHeap = []    # (capital, profit)
        maxHeap = []    # (-profit)
        for i in range(n):
            heapq.heappush(minHeap, (capital[i], profits[i]))
        for _ in range(k):
            while minHeap and minHeap[0][0] <= w:
                heapq.heappush(maxHeap, -heapq.heappop(minHeap)[1])
            if maxHeap:
                w += -heapq.heappop(maxHeap)
            else:
                break
        return w