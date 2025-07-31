# https://leetcode.com/problems/cheapest-flights-within-k-stops/description/

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # brute-force
        # TC: O(n^(k+1)), SC: O(k)
        graph = defaultdict(list)   # key (city) -> value ((neighbor, cost))
        for city, nei, cost in flights:
            graph[city].append((nei, cost))
        res = float('inf')
        def dfs(currCity, currCost, currStops):
            nonlocal res
            if currCity == dst:
                res = min(res, currCost)
                return
            if currStops > k:
                return
            for nei, cost in graph[currCity]:
                neiCost = currCost + cost
                if neiCost >= res:
                    continue
                dfs(nei, neiCost, currStops + 1)
        dfs(src, 0, 0)
        if res == float('inf'):
            return -1
        else:
            return res


        # better
        # TC: O(n*(k+1)), SC: O(n)
        graph = defaultdict(list)   # key (city) -> value ((neighbor, cost))
        for u, v, cost in flights:
            graph[u].append((v, cost))
        q = deque()
        q.append((src, 0, 0))   # (currCity, currCost, currStops)
        visited = [float('inf')] * n
        res = float('inf')
        while q:
            currCity, currCost, currStops = q.popleft()
            if currCity == dst:
                res = min(res, currCost)
                continue
            if currStops > k:
                continue
            for nei, cost in graph[currCity]:
                neiCost = currCost + cost
                if visited[nei] > neiCost:
                    visited[nei] = neiCost
                    q.append((nei, neiCost, currStops + 1))
        if res == float('inf'):
            return -1
        else:
            return res


        # optimal
        # TC: O(nlogn), SC: O(n)
        graph = defaultdict(list)   # key (city) -> value ((neighbor, cost))
        for u, v, cost in flights:
            graph[u].append((v, cost))
        minHeap = []    # (currCost, currCity, currStops)
        heapq.heappush(minHeap, (0, src, 0))
        while minHeap:
            currCost, currCity, currStops = heapq.heappop(minHeap)
            if currCity == dst:
                return currCost
            if currStops > k:
                continue
            for nei, cost in graph[currCity]:
                neiCost = currCost + cost
                heapq.heappush(minHeap, (neiCost, nei, currStops + 1))
        return -1