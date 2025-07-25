# https://leetcode.com/problems/minimum-height-trees/

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # brute-force
        # TC: O(n^2), SC: O(n)
        hashmap = {}    # key (node) -> value (height)
        graph = defaultdict(list)   # key (node) -> value (list of neighbors)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        def bfs(node):
            q = deque()
            q.append(node)
            visited = set()
            visited.add(node)
            currHeight = 0
            while q:
                for _ in range(len(q)):
                    currNode = q.popleft()
                    for neighbor in graph[currNode]:
                        if neighbor not in visited:
                            q.append(neighbor)
                            visited.add(neighbor)
                currHeight += 1
            return currHeight
        minHeight = sys.maxsize
        for node in range(n):
            hashmap[node] = bfs(node)
            minHeight = min(minHeight, hashmap[node])
        res = []
        for node, height in hashmap.items():
            if height == minHeight:
                res.append(node)
        return res


        # optimal
        # TC: O(n), SC: O(n)
        if n == 1:
            return [0]
        graph = defaultdict(list)   # key (node) -> value (neighbors)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        q = deque()
        edgesCount = {} # key (node) -> value (total edges)
        for node, neighbors in graph.items():
            if len(neighbors) == 1:
                q.append(node)
            edgesCount[node] = len(neighbors)
        while q:
            if n <= 2:
                return list(q)
            for _ in range(len(q)):
                currNode = q.popleft()
                n -= 1
                for neighbor in graph[currNode]:
                    edgesCount[neighbor] -= 1
                    if edgesCount[neighbor] == 1:
                        q.append(neighbor)