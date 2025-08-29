# https://leetcode.com/problems/redundant-connection/

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # brute-force (DFS)
        # TC: O(n^2), SC: O(n)
        def dfs(parent, node):
            if node in visited:
                return True
            visited.add(node)
            for nei in graph[node]:
                if nei == parent:
                    continue
                if dfs(node, nei):
                    return True
            return False
        graph = defaultdict(list)    # node -> list of neighbors
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            visited = set()
            if dfs(-1, u):
                return [u, v]


        # brute-force (BFS)
        # TC: O(n^2), SC: O(n)
        def bfs(node):
            q = deque()
            q.append((-1, node))
            visited = set()
            while q:
                parent, curr = q.popleft()
                if curr in visited:
                    return True
                visited.add(curr)
                for nei in graph[curr]:
                    if nei == parent:
                        continue
                    q.append((curr, nei))
            return False
        graph = defaultdict(list)    # node -> list of neighbors
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            if bfs(u):
                return [u, v]


        # optimal (disjoint-set union)
        # TC: O(n), SC: O(n)
        n = len(edges)
        parent = [u for u in range(n + 1)]
        rank = [0] * (n + 1)
        def findParent(u):
            if parent[u] != u:
                parent[u] = findParent(parent[u])
            return parent[u]
        def union(u, v):
            rootU = findParent(u)
            rootV = findParent(v)
            if rootU == rootV:
                return False
            else:
                if rank[rootU] > rank[rootV]:
                    parent[rootV] = rootU
                elif rank[rootU] < rank[rootV]:
                    parent[rootU] = rootV
                else:
                    parent[rootV] = rootU
                    rank[rootU] += 1
                return True
        for u, v in edges:
            if not union(u, v):
                return [u, v]