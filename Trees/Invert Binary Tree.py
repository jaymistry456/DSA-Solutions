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

        # Implement a queue starting with root    
        q = deque()
        q.append(root)
        while q:
            # Iterate over all the nodes at the current level
            for _ in range(len(q)):
                currNode = q.popleft()
                currNode.left, currNode.right = currNode.right, currNode.left
                if currNode.left:
                    q.append(currNode.left)
                if currNode.right:
                    q.append(currNode.right)
        
        return root