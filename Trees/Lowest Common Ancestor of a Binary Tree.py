# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # brute-force
        # TC: O(n), SC: O(height)
        def findPath(root, target, path):
            if not root:
                return False
            path.append(root)
            if root == target:
                return True
            if findPath(root.left, target, path) or findPath(root.right, target, path):
                return True
            path.pop()
            return False
        pathP = []
        pathQ = []
        findPath(root, p, pathP)
        findPath(root, q, pathQ)
        i = 0
        res = None
        while i < len(pathP) and i < len(pathQ):
            if pathP[i] == pathQ[i]:
                res = pathP[i]
                i += 1
            else:
                break
        return res

        # optimal
        # TC: O(n), SC: O(height)
        if root == p or root == q or root is None:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left or right