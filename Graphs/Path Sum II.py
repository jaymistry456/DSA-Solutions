# https://leetcode.com/problems/path-sum-ii/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        # # TC: O(n), SC: O(n)
        res = []
        currPath = []
        def dfs(curr, currSum):
            if not curr:
                return
            currPath.append(curr.val)
            currSum += curr.val
            if not curr.left and not curr.right:
                if currSum == targetSum:
                    res.append(currPath.copy())
            dfs(curr.left, currSum)
            dfs(curr.right, currSum)
            currPath.pop()
        dfs(root, 0)
        return res