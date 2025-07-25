# https://leetcode.com/problems/task-scheduler/description/

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # TC: O(n), SC: O(1)
        hashmap = defaultdict(int)  # key (task) -> value (-frequency)
        for task in tasks:
            hashmap[task] -= 1
        maxHeap = list(hashmap.values())    # max heap of frequency of tasks
        heapify(maxHeap)
        q = deque() # (-task frequency, time at which available)
        currTime = 0
        while maxHeap or q:
            currTime += 1
            while q and q[0][1] <= currTime:
                heappush(maxHeap, q.popleft()[0])
            if maxHeap:
                currTaskFreq = heappop(maxHeap)
                currTaskFreq += 1
                if currTaskFreq != 0:
                    q.append((currTaskFreq, currTime + n + 1))
        return currTime