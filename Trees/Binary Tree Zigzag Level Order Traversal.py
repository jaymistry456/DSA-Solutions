# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # TC: O(n), SC: O(n)
        if not root:
            return []
        def reverseArr(arr):
            l = 0
            r = len(arr) - 1
            while l < r:
                temp = arr[l]
                arr[l] = arr[r]
                arr[r] = temp
                l += 1
                r -= 1
        q = deque()
        q.append(root)
        leftToRight = True
        res = []
        while q:
            currLevel = []
            for _ in range(len(q)):
                currNode = q.popleft()
                currLevel.append(currNode.val)
                if currNode.left:
                    q.append(currNode.left)
                if currNode.right:
                    q.append(currNode.right)
            if not leftToRight:
                reverseArr(currLevel)
            res.append(currLevel)
            leftToRight = not leftToRight
        return res