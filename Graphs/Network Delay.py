# https://leetcode.com/problems/network-delay-time/

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # brute-force
        # TC: O(n!), SC: O(n)
        graph = defaultdict(list)    # node -> list of (nei, nei time)
        for u, v, w in times:
            graph[u].append((v, w))
        times = [float("inf")] * (n + 1)
        def dfs(currNode, currTime):
            if currTime >= times[currNode]:
                return
            times[currNode] = currTime
            for nei, neiTime in graph[currNode]:
                dfs(nei, currTime + neiTime)
        dfs(k, 0)
        res = max(times[1:])
        return res if res != float("inf") else -1

        
        # optimal
        # TC: O(nlogn), SC: O(n)
        graph = defaultdict(list)    # node -> list of (nei, nei time)
        for u, v, w in times:
            graph[u].append((v, w))
        minHeap = []    # (w, nei)
        heapq.heappush(minHeap, (0, k))
        visited = set()
        while minHeap:
            currTime, currNode = heapq.heappop(minHeap)
            if currNode in visited:
                continue
            visited.add(currNode)
            if len(visited) == n:
                return currTime
            for nei, neiDist in graph[currNode]:
                timeToNei = neiDist + currTime
                if nei not in visited:
                    heapq.heappush(minHeap, (timeToNei, nei))
        return -1