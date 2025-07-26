# https://leetcode.com/problems/top-k-frequent-words/description/

# brute-force
# TC: O(nlogn), SC: O(n)
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        n = len(words)
        hashmap = defaultdict(int)  # key (word) -> value (frequency)
        for i in range(n):
            hashmap[words[i]] += 1
        sortedWords = sorted(hashmap.items(), key=lambda x: (-x[1], x[0]))
        res = []
        for i in range(k):
            res.append(sortedWords[i][0])
        return res

        
# optimal
# TC: O(nlogk), SC: O(n)
class HeapItem:
    def __init__(self, word, count):
        self.word = word
        self.count = count

    def __lt__(self, compareTo):
        if self.count == compareTo.count:
            return self.word > compareTo.word
        return self.count < compareTo.count

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        n = len(words)
        hashmap = defaultdict(int)  # key (word) -> value (frequency)
        for i in range(n):
            hashmap[words[i]] += 1
        minHeap = []
        for word, freq in hashmap.items():
            item = HeapItem(word, freq)
            if len(minHeap) < k:
                heapq.heappush(minHeap, item)
            else:
                if item > minHeap[0]:
                    heapq.heappop(minHeap)
                    heapq.heappush(minHeap, item)
        res = []
        for _ in range(k):
            res.append(heapq.heappop(minHeap).word)
        return list(reversed(res))