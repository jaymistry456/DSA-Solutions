# https://neetcode.io/problems/valid-tree

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # DFS
        # TC: O(v+e), SC: O(v+e)
        if len(edges) != n - 1:
            return False
        graph = defaultdict(list)   # key (curr node) -> value (list of neighbors)
        for curr, nei in edges:
            graph[curr].append(nei)
            graph[nei].append(curr)
        visited = set()
        def dfs(prev, curr):
            if curr in visited:
                return False
            visited.add(curr)
            for nei in graph[curr]:
                if nei == prev:
                    # skip the parent
                    continue
                if not dfs(curr, nei):
                    return False
            return True
        return dfs(-1, 0) and len(visited) == n


        # BFS
        # TC: O(v+e), SC: O(v+e)
        if len(edges) != n - 1:
            return False
        graph = defaultdict(list)   # key (curr node) -> value (list of neighbors)
        for curr, nei in edges:
            graph[curr].append(nei)
            graph[nei].append(curr)
        q = deque()
        q.append((-1, 0))
        visited = set()
        while q:
            prev, curr = q.popleft()
            if curr in visited:
                return False
            visited.add(curr)
            for nei in graph[curr]:
                if nei == prev:
                    # skip the parent
                    continue
                if nei in visited:
                    return False
                q.append((curr, nei))
        return len(visited) == n


        # disjoint-set union
        # TC: O(v+e), SC: O(v)
        if len(edges) != n - 1:
            return False
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
        for u, v in edges:
            if not union(u, v):
                return False
        return True