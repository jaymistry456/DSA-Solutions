# https://www.geeksforgeeks.org/problems/inorder-successor-in-bst/1

'''
class Node:
    def __init__(self, val, k):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    # returns the inorder successor of the Node x in BST (rooted at 'root')
    def inorderSuccessor(self, root, x):
        # brute-force
        # TC: O(n), SC: O(n)
        nodes = []
        def dfs(curr):
            if not curr:
                return
            dfs(curr.left)
            nodes.append(curr.data)
            dfs(curr.right)
        dfs(root)
        for i in range(len(nodes)):
            if nodes[i] == x.data:
                if i + 1 < len(nodes):
                    return nodes[i + 1]
                else:
                    return -1
        return -1
        
        
        # optimal
        # TC: O(height), SC: O(1)
        res = None
        while root:
            if root.data <= x.data:
                root = root.right
            else:
                res = root.data
                root = root.left
        return res if res else -1