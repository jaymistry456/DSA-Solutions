# https://leetcode.com/problems/last-stone-weight/description/

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # TC: O(nlogn), SC: O(1)
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        while len(stones) >= 2:
            y = heapq.heappop(stones)
            x = heapq.heappop(stones)
            if y != x:
                heapq.heappush(stones, y - x)
        return -stones[-1] if stones else 0