# https://leetcode.com/problems/single-threaded-cpu/description/

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # TC: O(nlogn), SC: O(n)
        tasks = sorted((task[0], task[1], i) for i, task in enumerate(tasks))
        n = len(tasks)
        minHeap = []    # (processingTime, i)
        time = tasks[0][0]
        i = 0
        res = []
        while len(res) < n:
            while i < n and tasks[i][0] <= time:
                heapq.heappush(minHeap, (tasks[i][1], tasks[i][2]))
                i += 1
            if minHeap:
                prcoessingTime, currI = heapq.heappop(minHeap)
                time += prcoessingTime
                res.append(currI)
            else:
                time = tasks[i][0]
        return res