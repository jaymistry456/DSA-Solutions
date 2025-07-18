# https://leetcode.com/problems/balanced-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # brute-force
        # TC: O(n^2), SC: O(height)
        def height(node):
            if not node:
                return 0
            return 1 + max(height(node.left), height(node.right))
        
        if not root:
            return True
        left_height = height(root.left)
        right_height = height(root.right)
        if abs(left_height - right_height) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)


        # dfs
        # TC: O(n), SC: O(height)
        if not root:
            return True
        res = True  # assuming the tree is balanced
        
        def dfs(node):
            nonlocal res
            if not node:
                return 0
            left_height = dfs(node.left)
            right_height = dfs(node.right)
            if abs(left_height - right_height) > 1:
                res = False # res becomes False at any point the tree is imbalanced
            return 1 + max(left_height, right_height)

        dfs(root)
        return res