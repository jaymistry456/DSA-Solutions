# https://leetcode.com/problems/edit-distance/

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # brute-force
        # TC: O(2^(n1+n2)), SC: O(n1+n2)
        n1 = len(word1)
        n2 = len(word2)
        def dfs(i, j):
            if i == n1 and j == n2:
                return 0
            if i == n1:
                return n2 - j
            if j == n2:
                return n1 - i
            if word1[i] == word2[j]:
                return dfs(i + 1, j + 1)
            else:
                return 1 + min(dfs(i, j + 1), dfs(i + 1, j + 1), dfs(i + 1, j))
        return dfs(0, 0)


        # optimal
        # TC: O(n1*n2), SC: O(n1*n2)
        n1 = len(word1)
        n2 = len(word2)
        dp = {}    # (i, j) -> min cost to convert text1[i:] to text2[j:]
        def dfs(i, j):
            if i == n1 and j == n2:
                return 0
            if i == n1:
                return n2 - j
            if j == n2:
                return n1 - i
            if (i, j) in dp:
                return dp[(i, j)]
            if word1[i] == word2[j]:
                dp[(i, j)] = dfs(i + 1, j + 1)
            else:
                dp[(i, j)] = 1 + min(dfs(i, j + 1), dfs(i + 1, j + 1), dfs(i + 1, j))
            return dp[(i, j)]
        return dfs(0, 0)