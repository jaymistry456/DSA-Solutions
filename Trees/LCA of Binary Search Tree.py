# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # recursive
        # TC: O(height), SC: O(height)
        if not root or not p or not q:
            return None
        if p.val <= root.val <= q.val or p.val >= root.val >= q.val:
            return root
        elif root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return self.lowestCommonAncestor(root.left, p, q)


        # iterative
        # TC: O(height), SC: O(1)
        while root:
            if p.val <= root.val <= q.val or p.val >= root.val >= q.val:
                return root
            elif root.val < p.val and root.val < q.val:
                root = root.right
            else:
                root = root.left
        return None