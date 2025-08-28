# https://neetcode.io/problems/count-connected-components

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # DFS
        # TC: O(n), SC: O(n)
        graph = defaultdict(list)    # node -> list of neighbors
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = set()
        def dfs(u):
            visited.add(u)
            for nei in graph[u]:
                if nei not in visited:
                    dfs(nei)
        res = 0
        for u in range(n):
            if u not in visited:
                res += 1
                dfs(u)
        return res


        # BFS
        # TC: O(n), SC: O(n)
        graph = defaultdict(list)    # node -> list of neighbours
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = set()
        def bfs(u):
            visited.add(u)
            q = deque()
            q.append(u)
            while q:
                curr = q.popleft()
                for nei in graph[curr]:
                    if nei not in visited:
                        q.append(nei)
                        visited.add(nei)
        res = 0
        for u in range(n):
            if u not in visited:
                res += 1
                bfs(u)
        return res


        # disjoint-set union
        # TC: O(n), SC: O(n)
        parent = [u for u in range(n)]
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
                    parent[rootV] = rootU
                    rank[rootU] += 1
                return True
        res = n
        for u, v in edges:
            if union(u, v):
                res -= 1
        return res