# https://leetcode.com/problems/the-kth-factor-of-n/

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        # TC: O(sqrt(n)), SC: O(k)
        maxHeap = []    # -factor
        for num in range(1, int(math.sqrt(n)) + 1):
            if n % num == 0:
                heapq.heappush(maxHeap, -num)
                if len(maxHeap) > k:
                    heapq.heappop(maxHeap)
                if n // num != num:
                    heapq.heappush(maxHeap, -n // num)
                    if len(maxHeap) > k:
                        heapq.heappop(maxHeap)
        return -maxHeap[0] if len(maxHeap) == k else -1