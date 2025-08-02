# https://leetcode.com/problems/find-median-from-data-stream/description/

# brute-force
class MedianFinder:

    def __init__(self):
        self.nums = []

    # TC: O(1), SC: O(n)
    def addNum(self, num: int) -> None:
        self.nums.append(num)

    # TC: O(nlogn), SC: O(n)
    def findMedian(self) -> float:
        self.nums.sort()
        n = len(self.nums)
        if n % 2 == 1:
            return self.nums[n // 2]
        else:
            return (self.nums[n // 2 - 1] + self.nums[n // 2]) / 2


# optimal
class MedianFinder:

    def __init__(self):
        self.minHeap = []    # for the larger half
        self.maxHeap = []    # for the smaller half

    # TC: O(logn), SC: O(n)
    def addNum(self, num: int) -> None:
        def balanceHeaps():
            minLen = len(self.minHeap)
            maxLen = len(self.maxHeap)
            if minLen - maxLen > 1:
                heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))
            elif maxLen - minLen > 1:
                heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
        if self.minHeap and num > self.minHeap[0]:
            heapq.heappush(self.minHeap, num)
        else:
            heapq.heappush(self.maxHeap, -num)
        balanceHeaps()

    # TC: O(1), SC: O(n)
    def findMedian(self) -> float:
        minLen = len(self.minHeap)
        maxLen = len(self.maxHeap)
        if minLen > maxLen:
            return self.minHeap[0]
        elif minLen < maxLen:
            return -self.maxHeap[0]
        else:
            return (-self.maxHeap[0] + self.minHeap[0]) / 2




# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()