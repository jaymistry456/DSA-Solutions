# https://leetcode.com/problems/palindrome-partitioning/description/

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # TC: O(n*2^n), SC: O(n)
        currRes = []
        res = []
        n = len(s)
        def helper(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        def dfs(i):
            if i == n:
                res.append(currRes.copy())
                return
            for j in range(i, n):
                if helper(i, j):
                    currRes.append(s[i:j+1])
                    dfs(j + 1)
                    currRes.pop()
        dfs(0)
        return res