# https://leetcode.com/problems/path-sum-iii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # brute-force
        # TC: O(n^2), SC: O(height)
        res = 0
        def dfs(currNode, currSum):
            nonlocal res
            if not currNode:
                return
            currSum += currNode.val
            if currSum == targetSum:
                res += 1
            dfs(currNode.left, currSum)
            dfs(currNode.right, currSum)
        currNode = root
        def traversal(currNode):
            if not currNode:
                return
            dfs(currNode, 0)
            traversal(currNode.left)
            traversal(currNode.right)
        traversal(root)
        return res


        # optimal
        # TC: O(n), SC: O(n)
        hashmap = {}    # key (currSum) -> value (total paths that have this currSum)
        hashmap[0] = 1  # base case: we have 1 path which has sum 0
        res = 0
        def dfs(currNode, currSum):
            nonlocal res
            if not currNode:
                return
            currSum += currNode.val
            if currSum -targetSum in hashmap:
                res += hashmap[currSum - targetSum]
            if currSum in hashmap:
                hashmap[currSum] += 1
            else:
                hashmap[currSum] = 1
            dfs(currNode.left, currSum)
            dfs(currNode.right, currSum)
            hashmap[currSum] -= 1   # backtracking
        dfs(root, 0)
        return res