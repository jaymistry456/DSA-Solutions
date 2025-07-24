# https://leetcode.com/problems/word-break/description/

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # brute-force
        # Tc: O(2^n), SC: O(n)
        n = len(s)
        hashset = set(wordDict)
        def dfs(i):
            if i == n:
                return True
            for j in range(i, n):
                currWord = s[i:j+1]
                if currWord in hashset and dfs(j + 1):
                    return True
            return False
        return dfs(0)


        # optimal
        # TC: O(n^2), SC: O(n)
        n = len(s)
        hashset = set(wordDict)
        dp = {} # key (i) -> value (True or False)
        def dfs(i):
            if i == n:
                return True
            if i in dp:
                return dp[i]
            for j in range(i, n):
                currWord = s[i:j+1]
                if currWord in hashset and dfs(j + 1):
                    dp[i] = True
                    return True
            dp[i] = False
            return False
        return dfs(0)