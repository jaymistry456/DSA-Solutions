# https://leetcode.com/problems/clone-graph/description/

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # DFS
        # TC: O(n), SC: O(n)
        if not node:
            return None
        hashmap = {}    # key (original node) -> value (new node)
        def dfs(node):
            hashmap[node] = Node(node.val)
            for neighbor in node.neighbors:
                if neighbor not in hashmap:
                    dfs(neighbor)
        dfs(node)
        for node1, node2 in hashmap.items():
            for neighbor in node1.neighbors:
                node2.neighbors.append(hashmap[neighbor])
        return hashmap[node]


        # BFS
        # TC: O(n), SC: O(n)
        if not node:
            return None
        q = deque()
        q.append(node)
        hashmap = {}    # key (original node) -> value (new node)
        while q:
            currNode = q.popleft()
            hashmap[currNode] = Node(currNode.val)
            for neighbor in currNode.neighbors:
                if neighbor not in hashmap:
                    q.append(neighbor)
        for node1, node2 in hashmap.items():
            for neighbor in node1.neighbors:
                node2.neighbors.append(hashmap[neighbor])
        return hashmap[node]