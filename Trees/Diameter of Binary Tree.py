# https://leetcode.com/problems/diameter-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # brute-force
        # TC: O(n^2), SC: O(n)
        def height(node):
            if not node:
                return 0
            return 1 + max(height(node.left), height(node.right))

        def diameter(node):
            if not node:
                return 0
            left_height = height(node.left)
            right_height = height(node.right)
            curr_diameter = left_height + right_height
            left_diameter = diameter(node.left) # recursively calculate diamter from left subtree
            right_diameter = diameter(node.right)   # recursively calculate diamter from right subtree
            return max(curr_diameter, left_diameter, right_diameter)
        return diameter(root)


        # optimal
        # TC: O(n), SC: O(n)
        res = 0
        def max_height(node):
            nonlocal res
            if not node:
                return 0
            left_height = max_height(node.left)
            right_height = max_height(node.right)
            res = max(res, left_height + right_height)
            return 1 + max(left_height, right_height)
        max_height(root)
        return res