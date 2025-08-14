# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # TC: O(n), SC: O(height)
        def dfs(curr):
            if not curr:
                return None
            leftTail = dfs(curr.left)
            rightTail = dfs(curr.right)
            if leftTail:
                leftTail.right = curr.right
                curr.right = curr.left
                curr.left = None
            return rightTail or leftTail or curr    # reverse preorder
        dfs(root)