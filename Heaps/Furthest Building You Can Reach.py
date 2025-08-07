# https://leetcode.com/problems/furthest-building-you-can-reach/

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        # brute-force
        # TC: O(2^n), SC: O(n)
        n = len(heights)
        def dfs(i, currBricks, currLadders):
            if i == n - 1:
                return i
            currDiff = heights[i + 1] - heights[i]
            if currDiff < 0:
                return dfs(i + 1, currBricks, currLadders)
            res = i
            if currDiff <= currBricks:
                res = max(res, dfs(i + 1, currBricks - currDiff, currLadders))
            if currLadders > 0:
                res = max(res, dfs(i + 1, currBricks, currLadders - 1))
            return res
        return dfs(0, bricks, ladders)


        # better
        # TC: O(n*b*l), SC: O(n)
        n = len(heights)
        dp = {}    # (i, currBricks, currLadders) -> max index
        def dfs(i, currBricks, currLadders):
            if i == n - 1:
                return i
            if (i, currBricks, currLadders) in dp:
                return dp[(i, currBricks, currLadders)]
            currDiff = heights[i + 1] - heights[i]
            if currDiff < 0:
                dp[(i, currBricks, currLadders)] = dfs(i + 1, currBricks, currLadders)
                return dfs(i + 1, currBricks, currLadders)
            dp[(i, currBricks, currLadders)] = i
            if currDiff <= currBricks:
                dp[(i, currBricks, currLadders)] = max(dp[(i, currBricks, currLadders)], dfs(i + 1, currBricks - currDiff, currLadders))
            if currLadders > 0:
                dp[(i, currBricks, currLadders)] = max(dp[(i, currBricks, currLadders)], dfs(i + 1, currBricks, currLadders - 1))
            return dp[(i, currBricks, currLadders)]
        return dfs(0, bricks, ladders)



        optimal
        # TC: O(nlogn), SC: O(n)
        i = 0
        n = len(heights)
        maxHeap = []    # stores height differences
        while i < n - 1:
            currDiff = heights[i + 1] - heights[i]
            if currDiff > 0:
                heapq.heappush(maxHeap, -currDiff)
                bricks -= currDiff
                if bricks < 0:
                    if ladders > 0:
                        ladders -= 1
                        bricks += -heapq.heappop(maxHeap)
                    else:
                        return i
            i += 1
        # return n - 1


        # optimal
        # TC: O(nlogl), SC: O(l)
        n = len(heights)
        minHeap = []    # min differences
        i = 0
        while i < n:
            if i < n - 1:
                currDiff = heights[i + 1] - heights[i]
                if currDiff > 0:
                    heapq.heappush(minHeap, currDiff)
                    if len(minHeap) > ladders:
                        bricks -= heapq.heappop(minHeap)
                        if bricks < 0:
                            return i
            i += 1
        return n - 1