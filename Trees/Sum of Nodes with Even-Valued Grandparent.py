# https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        # DFS
        # Tc: O(n), SC: O(height)
        def dfs(grandParent, parent, curr):
            if not curr:
                return 0
            res = 0
            if grandParent and grandParent.val % 2 == 0:
                res = curr.val
            res += dfs(parent, curr, curr.left)
            res += dfs(parent, curr, curr.right)
            return res
        return dfs(None, None, root)


        # BFS
        # TC: O(n), SC: O(n)
        if not root:
            return 0
        q = deque()    # (grandParent, parent, curr)
        q.append((None, None, root))
        res = 0
        while q:
            grandParent, parent, curr = q.popleft()
            if grandParent and grandParent.val % 2 == 0:
                res += curr.val
            if curr.left:
                q.append((parent, curr, curr.left))
            if curr.right:
                q.append((parent, curr, curr.right))
        return res