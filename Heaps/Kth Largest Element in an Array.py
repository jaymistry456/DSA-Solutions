# https://leetcode.com/problems/kth-largest-element-in-an-array/

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # brute-force
        # TC: O(nlogn), SC: O(1)
        return sorted(nums)[len(nums) - k]


        # optimal
        # TC: O(nlogk), SC: O(k)
        minHeap = []
        for i in range(len(nums)):
            heapq.heappush(minHeap, nums[i])
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        return minHeap[0]