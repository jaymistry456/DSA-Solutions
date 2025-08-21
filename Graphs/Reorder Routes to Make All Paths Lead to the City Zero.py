# https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # DFS
        # TC: O(n), SC: O(n)
        graph = defaultdict(list)    # u -> (v, cost), cost = 1 for normal and 0 for reverse
        for u, v in connections:
            graph[u].append((v, 1))
            graph[v].append((u, 0))
        visited = set()
        visited.add(0)
        def dfs(u):
            curr = 0
            for nei, cost in graph[u]:
                if nei not in visited:
                    visited.add(nei)
                    curr += cost
                    curr += dfs(nei)
            return curr
        return dfs(0)


        # BFS
        # TC: O(n), SC: O(n)
        graph = defaultdict(list)    # u -> (v, cost), cost = 1 for normal and 0 for reverse
        for u, v in connections:
            graph[u].append((v, 1))
            graph[v].append((u, 0))
        visited = set()
        visited.add(0)
        q = deque()
        q.append((0, 0))
        res = 0
        while q:
            curr, currCost = q.popleft()
            for nei, neiCost in graph[curr]:
                if nei not in visited:
                    res += neiCost
                    q.append((nei, neiCost))
                    visited.add(nei)
        return res