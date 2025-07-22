# https://leetcode.com/problems/validate-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # brute-force
        # TC: O(n), SC: O(n)
        inorder = []
        def inorderTraversal(node):
            if not node:
                return
            inorderTraversal(node.left)
            inorder.append(node.val)
            inorderTraversal(node.right)
        inorderTraversal(root)
        for i in range(len(inorder) - 1):
            if inorder[i] >= inorder[i + 1]:
                return False
        return True


        # optimal
        # TC: O(n), SC: O(height)
        def dfs(node, leftMin, rightMax):
            if not node:
                return True
            return leftMin < node.val < rightMax and dfs(node.left, leftMin, node.val) and dfs(node.right, node.val, rightMax)
        return dfs(root, -sys.maxsize, sys.maxsize)