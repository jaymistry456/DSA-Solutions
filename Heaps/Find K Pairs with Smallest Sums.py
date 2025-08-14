# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # brute-force
        # TC: O(n^2*logn), SC: O(n)
        arr = []    # [sum, num1, num2]
        for num1 in nums1:
            for num2 in nums2:
                arr.append([num1 + num2, num1, num2])
        arr.sort(key=lambda x:x[0])
        res = []
        for i in range(k):
            res.append([arr[i][1], arr[i][2]])
        return res


        # better
        # TC: O(n^2*logk), SC: O(k)
        maxHeap = []    # [-sum, num1, nums2]
        for num1 in nums1:
            for num2 in nums2:
                heapq.heappush(maxHeap, [-num1 - num2, num1, num2])
                if len(maxHeap) > k:
                    heapq.heappop(maxHeap)
        res = []
        for i in range(len(maxHeap)):
            sum, num1, num2 = heapq.heappop(maxHeap)
            res.append([num1, num2])
        return res


        # optimal
        # TC: O(klogk), SC: O(k)
        res = []
        i = 0
        j = 0
        minHeap = []    # (sum, i, j)
        visited = set()
        heapq.heappush(minHeap, (nums1[0] + nums2[0], 0, 0))
        visited.add((0, 0))
        for _ in range(k):
            sum, i, j = heapq.heappop(minHeap)
            res.append([nums1[i], nums2[j]])
            if i + 1 < len(nums1) and (i + 1, j) not in visited:
                heapq.heappush(minHeap, (nums1[i + 1] + nums2[j], i + 1, j))
                visited.add((i + 1, j))
            if j + 1 < len(nums2) and (i, j + 1) not in visited:
                heapq.heappush(minHeap, (nums1[i] + nums2[j + 1], i, j + 1))
                visited.add((i, j + 1))
        return res