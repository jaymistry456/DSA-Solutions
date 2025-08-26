# https://neetcode.io/problems/valid-tree

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # DFS
        # TC: O(n), SC: O(n)
        if len(edges) != n - 1:
            return False
        graph = defaultdict(list)    # node -> list of neighbors
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = set()
        def dfs(parent, currNode):
            if currNode in visited:
                return False
            visited.add(currNode)
            for nei in graph[currNode]:
                if nei == parent:
                    continue
                if not dfs(currNode, nei):
                    return False
            return True
        res = dfs(-1, 0)
        return res and len(visited) == n


        # BFS
        # TC: O(n), SC: O(n)
        if len(edges) != n - 1:
            return False
        graph = defaultdict(list)    # node -> list of neighbors
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        q = deque()    # (parent, node)
        visited = set()
        q.append((-1, 0))
        while q:
            parent, node = q.popleft()
            if node in visited:
                return False
            visited.add(node)
            for nei in graph[node]:
                if nei == parent:
                    continue
                q.append((node, nei))
        return len(visited) == n


        # disjoint-set union
        # TC: O(n), SC: O(n)
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