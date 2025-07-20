# https://leetcode.com/problems/symmetric-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # DFS
        # TC: O(n), SC: O(height)
        def dfs(left, right):
            if not left and not right:
                return True
            elif not left or not right:
                return False
            else:
                return left.val == right.val and dfs(left.left, right.right) and dfs(left.right, right.left)
        return dfs(root.left, root.right)


        # BFS
        # TC: O(n), SC: O(n)
        q = deque()
        q.append((root.left, root.right))
        while q:
            left, right = q.popleft()
            if not left and not right:
                continue
            elif not left or not right:
                return False
            else:
                if left.val != right.val:
                    return False
                q.append((left.left, right.right))
                q.append((left.right, right.left))
        return True