# https://leetcode.com/problems/maximum-width-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # TC: O(n), SC: O(n)
        if not root:
            return 0
        q = deque()
        q.append((root, 1))
        res = 0
        while q:
            minVal = float("inf")
            maxVal = float("-inf")
            for _ in range(len(q)):
                curr, n = q.popleft()
                minVal = min(minVal, n)
                maxVal = max(maxVal, n)
                if curr.left:
                    q.append((curr.left, 2 * n))
                if curr.right:
                    q.append((curr.right, 2 * n + 1))
            res = max(res, maxVal - minVal + 1)
        return res