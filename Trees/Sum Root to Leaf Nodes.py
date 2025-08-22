# https://leetcode.com/problems/sum-root-to-leaf-numbers/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # Tc: O(n), SC: O(height)
        if not root:
            return 0
        def dfs(currNum, currNode):
            if not currNode.left and not currNode.right:
                return currNum
            res = 0
            if currNode.left:
                res += dfs(currNum * 10 + currNode.left.val, currNode.left)
            if currNode.right:
                res += dfs(currNum * 10 + currNode.right.val, currNode.right)
            return res
        return dfs(root.val, root)