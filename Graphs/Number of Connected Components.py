# https://neetcode.io/problems/count-connected-components

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # DFS
        # TC: O(v+e), SC: O(v+e)
        graph = defaultdict(list)   # key (node) -> value (neighbors of node)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = set()
        def dfs(curr):
            visited.add(curr)
            for nei in graph[curr]:
                if nei not in visited:
                    dfs(nei)
        res = 0
        for node in range(n):
            if node not in visited:
                dfs(node)
                res += 1
        return res


        # BFS
        # TC: O(v+e), SC: O(v+e)
        graph = defaultdict(list)   # key (node) -> value (neighbors of node)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = set()
        def bfs(curr):
            visited.add(curr)
            q = deque()
            q.append(curr)
            while q:
                node = q.popleft()
                for nei in graph[node]:
                    if nei not in visited:
                        q.append(nei)
                        visited.add(nei)
        res = 0
        for node in range(n):
            if node not in visited:
                bfs(node)
                res += 1
        return res


        # disjoint-set union
        # TC: O(v+e), SC: O(v)
        parent = [node for node in range(n)]
        rank = [0] * n
        def findParent(u):
            if parent[u] != u:
                parent[u] = findParent(parent[u])
            return parent[u]
        def union(u, v):
            rootU = findParent(u)
            rootV = findParent(v)
            if rootU == rootV:
                # cycle detected
                return False
            else:
                if rank[rootU] > rank[rootV]:
                    parent[rootV] = rootU
                elif rank[rootU] < rank[rootV]:
                    parent[rootU] = rootV
                else:
                    parent[rootV] = parent[rootU]
                    rank[rootU] += 1
                return True
        res = n
        for u, v in edges:
            if union(u, v):
                res -= 1
        return res