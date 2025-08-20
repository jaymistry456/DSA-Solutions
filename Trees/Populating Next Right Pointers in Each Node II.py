# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/description/

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # TC: O(n), SC: O(n)
        if not root:
            return root
        q = deque([root])
        while q:
            currLevel = []
            for _ in range(len(q)):
                curr = q.popleft()
                currLevel.append(curr)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            for i in range(len(currLevel) - 1):
                currLevel[i].next = currLevel[i + 1]
        return root