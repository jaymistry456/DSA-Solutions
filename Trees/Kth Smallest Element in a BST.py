# https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # brute-force
        # TC: O(nlogn), SC: O(n)
        arr = []
        def dfs(node):
            if not node:
                return
            arr.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        arr.sort()
        return arr[k - 1]


        # better
        # TC: O(n), SC: O(n)
        arr = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            arr.append(node.val)
            dfs(node.right)
        dfs(root)
        return arr[k - 1]
    
        # optimal
        # TC: O(n), SC: O(height)
        i = 0
        res = None
        def dfs(curr):
            nonlocal i, res
            if not curr:
                return
            dfs(curr.left)
            i += 1
            if i == k:
                res = curr.val
                return
            dfs(curr.right)
        dfs(root)
        return res