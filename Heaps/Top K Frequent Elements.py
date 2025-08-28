# https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # brute-force
        # TC: O(nlogn), SC: O(n)
        hashmap = defaultdict(int)    # num -> freq of num
        for num in nums:
            hashmap[num] += 1
        maxHeap = []    # (-freq, num)
        for num, freq in hashmap.items():
            heapq.heappush(maxHeap, (-freq, num))
        res = []
        for _ in range(k):
            res.append(heapq.heappop(maxHeap)[1])
        return res


        # optimal (heap-based)
        # TC: O(nlogk), SC: o(k)
        hashmap = defaultdict(int)    # num -> freq of num
        for num in nums:
            hashmap[num] += 1
        minHeap = []    # (freq, num)
        for num, freq in hashmap.items():
            heapq.heappush(minHeap, (freq, num))
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        res = []
        while minHeap:
            res.append(heapq.heappop(minHeap)[1])
        return res


        # optimal (bucket sort)
        # TC: O(n + maxfreq), SC: o(n)
        hashmap = defaultdict(int)    # num -> freq of num
        for num in nums:
            hashmap[num] += 1
        bucket = [[] for _ in range(max(hashmap.values()) + 1)]    # freq -> list of nums
        for num, freq in hashmap.items():
            bucket[freq].append(num)
        res = []
        for i in range(len(bucket) - 1, -1, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res