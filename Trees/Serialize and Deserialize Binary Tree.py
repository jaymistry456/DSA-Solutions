# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    # TC: O(n), SC: O(height)
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        def dfs(curr):
            if not curr:
                res.append('N')
                return
            res.append(str(curr.val))
            dfs(curr.left)
            dfs(curr.right)
        dfs(root)
        return ','.join(res)

    # TC: O(n), SC: O(height)
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        values = data.split(',')
        i = 0
        def dfs():
            nonlocal i
            if values[i] == 'N':
                i += 1
                return None
            root = TreeNode(int(values[i]))
            i += 1
            root.left = dfs()
            root.right = dfs()
            return root
        return dfs()
            

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))