# https://leetcode.com/problems/binary-tree-maximum-path-sum/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # brute-force
        # TC: O(n^2), SC: O(height)
        def helper(curr):
            if not curr:
                return 0
            return curr.val + max(helper(curr.left), helper(curr.right), 0)
        def dfs(curr):
            if not curr:
                return float('-inf')
            leftSum = max(helper(curr.left), 0)
            rightSum = max(helper(curr.right), 0)
            return max(curr.val + leftSum + rightSum, dfs(curr.left), dfs(curr.right))
        return dfs(root)


        # optimal
        # TC: O(n), SC: O(height)
        res = float('-inf')
        def dfs(curr):
            nonlocal res
            if not curr:
                return float('-inf')
            leftSum = max(dfs(curr.left), 0)
            rightSum = max(dfs(curr.right), 0)
            res = max(res, curr.val + leftSum + rightSum)
            return curr.val + max(leftSum, rightSum)
        dfs(root)
        return res