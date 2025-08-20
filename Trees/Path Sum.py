# https://leetcode.com/problems/path-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # TC: O(n), SC: O(height)
        if not root:
            return False
        def dfs(curr, currSum):
            if curr.left and curr.right:
                return dfs(curr.left, currSum + curr.left.val) or dfs(curr.right, currSum + curr.right.val)
            elif curr.left:
                return dfs(curr.left, currSum + curr.left.val)
            elif curr.right:
                return dfs(curr.right, currSum + curr.right.val)
            else:
                return currSum == targetSum
        return dfs(root, root.val)