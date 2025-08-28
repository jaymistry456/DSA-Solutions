# https://leetcode.com/problems/interleaving-string/

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # brute-force
        # TC: O(2^(n1+n2)), SC: O(n1+n2)
        n1 = len(s1)
        n2 = len(s2)
        n3 = len(s3)
        if n1 + n2 != n3:
            return False
        def dfs(i, j):
            if i == n1 and j == n2:
                return True
            if i > n1:
                return False
            if j > n2:
                return False
            if i < n1 and s1[i] == s3[i + j] and dfs(i + 1, j):
                return True
            if j < n2 and s2[j] == s3[i + j] and dfs(i, j + 1):
                return True
            return False
        return dfs(0, 0)


        # optimal
        # TC: O(n1*n2), SC: O(n1*n2)
        n1 = len(s1)
        n2 = len(s2)
        n3 = len(s3)
        if n1 + n2 != n3:
            return False
        dp = {}    # (i, j) -> True/False
        def dfs(i, j):
            if i == n1 and j == n2:
                return True
            if i > n1:
                return False
            if j > n2:
                return False
            if (i, j) in dp:
                return dp[(i, j)]
            if i < n1 and s1[i] == s3[i + j] and dfs(i + 1, j):
                dp[(i, j)] = True
                return True
            if j < n2 and s2[j] == s3[i + j] and dfs(i, j + 1):
                dp[(i, j)] = True
                return True
            dp[(i, j)] = False
            return dp[(i, j)]
        return dfs(0, 0)