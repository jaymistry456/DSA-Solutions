# https://leetcode.com/problems/binary-tree-right-side-view/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # TC: O(n), SC: O(n)
        if not root:
            return []
        q = deque()
        q.append(root)
        res = []
        while q:
            qLength = len(q)
            for i in range(qLength):
                curr = q.popleft()
                if i == qLength - 1:
                    res.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
        return res