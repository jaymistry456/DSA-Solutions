# https://leetcode.com/problems/minimum-absolute-difference-in-bst/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # TC: O(n), SC: O(height)
        def dfs(curr, minVal, maxVal):
            if not curr:
                return maxVal - minVal
            return min(dfs(curr.left, minVal, curr.val), dfs(curr.right, curr.val, maxVal))
        return dfs(root, float("-inf"), float("inf"))