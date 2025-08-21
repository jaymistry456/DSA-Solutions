# https://leetcode.com/problems/reconstruct-itinerary/description/

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # TC: O(nlogn), SC: O(n)
        graph = defaultdict(list)    # src -> dst in alphabetical order (minHeap)
        for u, v in tickets:
            heapq.heappush(graph[u], v)
        res = []
        def dfs(u):
            while graph[u]:
                v = heapq.heappop(graph[u])
                dfs(v)
            res.append(u)
        dfs("JFK")
        return res[::-1]