# https://leetcode.com/problems/invert-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # DFS
        # TC: O(n), SC: O(height)
        if not root:
            return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

        # BFS
        # TC: O(n), SC: O(n)
        if not root:
            return None
        q = deque()
        q.append(root)
        while q:
            currNode = q.popleft()
            temp = currNode.left
            currNode.left = currNode.right
            currNode.right = temp
            if currNode.left:
                q.append(currNode.left)
            if currNode.right:
                q.append(currNode.right)
        return root