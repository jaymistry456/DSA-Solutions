# https://leetcode.com/problems/longest-common-subsequence/

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # brute-force
        # TC: O(2^(n1+n2)), SC: O(n1+n2)
        n1 = len(text1)
        n2 = len(text2)
        def dfs(i, j):
            if i >= n1 or j >= n2:
                return 0
            if text1[i] == text2[j]:
                return 1 + dfs(i + 1, j + 1)
            else:
                return max(dfs(i + 1, j), dfs(i, j + 1))
        return dfs(0, 0)


        # optimal
        # TC: O(n1*n2), SC: O(n1*n2)
        n1 = len(text1)
        n2 = len(text2)
        dp = {}    # (i, j) -> LCS from (i, j)
        def dfs(i, j):
            if i >= n1 or j >= n2:
                return 0
            if (i, j) in dp:
                return dp[(i, j)]
            if text1[i] == text2[j]:
                dp[(i, j)] = 1 + dfs(i + 1, j + 1)
            else:
                dp[(i, j)] = max(dfs(i + 1, j), dfs(i, j + 1))
            return dp[(i, j)]
        return dfs(0, 0)