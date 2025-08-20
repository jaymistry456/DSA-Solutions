# https://leetcode.com/problems/number-of-provinces/description/

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # DFS
        # TC: O(n^2), SC: O(n)
        visited = set()
        n = len(isConnected)
        res = 0
        def dfs(node):
            visited.add(node)
            for nei in range(n):
                if nei not in visited and isConnected[node][nei] == 1:
                    dfs(nei)
        for node in range(n):
            if node not in visited:
                dfs(node)
                res += 1
        return res


        # BFS
        # TC: O(n^2), SC: O(n)
        visited = set()
        n = len(isConnected)
        res = 0
        def bfs(node):
            q = deque([node])
            visited.add(node)
            while q:
                curr = q.popleft()
                for nei in range(n):
                    if nei not in visited and isConnected[curr][nei] == 1:
                        q.append(nei)
                        visited.add(nei)
        for node in range(n):
            if node not in visited:
                bfs(node)
                res += 1
        return res


        # disjoint-set union
        # TC: O(n^2), SC: O(n)
        n = len(isConnected)
        rank = [0] * n
        parent = [u for u in range(n)]
        res = n
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
        for u in range(n):
            for v in range(n):
                if isConnected[u][v] == 1 and union(u, v):
                    res -= 1
        return res