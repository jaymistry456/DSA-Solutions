# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # brute-force
        # TC: O(n^2), SC: O(n)
        if not inorder:
            return None
        root = TreeNode(postorder[-1])
        mid = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[:mid], postorder[:mid])
        root.right = self.buildTree(inorder[mid+1:], postorder[mid:len(postorder)-1])
        return root


        # optimal
        # TC: O(n), SC: O(n)
        hashmap = {}   # node -> index of node in inorder
        for i in range(len(inorder)):
            hashmap[inorder[i]] = i
        postIndex = len(postorder) - 1
        def helper(l, r):
            if l > r:
                return None
            nonlocal postIndex
            rootVal = postorder[postIndex]
            postIndex -= 1
            root = TreeNode(rootVal)
            mid = hashmap[rootVal]
            root.right = helper(mid + 1, r)
            root.left = helper(l, mid - 1)
            return root
        return helper(0, len(postorder) - 1)