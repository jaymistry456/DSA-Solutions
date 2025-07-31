# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # TC: O(n), SC: O(n)
        # DFS traversal to set parent of every node
        hashmap = {}    # key (node) -> value (parent of node)
        def dfs(curr, parent):
            if not curr:
                return
            hashmap[curr] = parent
            dfs(curr.left, curr)
            dfs(curr.right, curr)
        dfs(root, None)
        # BFS level order traversal on 3 directions: left, right and parent
        q = deque()
        q.append((target, 0))   # (curr node, curr dist)
        visited = set()
        visited.add(target)
        res = []
        while q:
            for _ in range(len(q)):
                curr, dist = q.popleft()
                if dist == k:
                    res.append(curr.val)
                else:
                    for nei in [curr.left, curr.right, hashmap[curr]]:
                        if nei and nei not in visited:
                            q.append((nei, dist + 1))
                            visited.add(nei)
        return res