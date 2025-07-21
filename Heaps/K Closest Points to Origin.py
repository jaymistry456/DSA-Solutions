# https://leetcode.com/problems/k-closest-points-to-origin/description/

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # brute-force
        # TC: O(nlogn), SC: O(1)
        arr = []
        for x, y in points:
            arr.append((x ** 2 + y ** 2, x, y))
        arr.sort(key = lambda x: x[0])
        res = []
        for i in range(k):
            res.append([arr[i][1], arr[i][2]])
        return res


        # better
        # TC: O(klogn), SC: O(n)
        minHeap = []
        for x, y in points:
            heapq.heappush(minHeap, (x ** 2 + y ** 2, x, y))
        heapq.heapify(minHeap)
        res = []
        for _ in range(k):
            distance, x, y = heapq.heappop(minHeap)
            res.append([x, y])
        return res

        # optimal
        # TC: O(nlogk), SC: O(k)
        maxHeap = []
        for x, y in points:
            heapq.heappush(maxHeap, (-x ** 2 - y ** 2, x, y))
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        res = []
        for i in range(k):
            distance, x, y = heapq.heappop(maxHeap)
            res.append([x, y])
        return res