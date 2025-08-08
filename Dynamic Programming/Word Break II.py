# https://leetcode.com/problems/word-break-ii/

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # brute-force
        # TC: O(2^n*n^2), SC: O(2^n*n)
        n = len(s)
        hashset = set(wordDict)
        currRes = []
        res = []
        def dfs(i):
            if i == n:
                res.append(" ".join(currRes))
                return
            for j in range(i, n):
                substr = s[i:j+1]
                if substr in hashset:
                    currRes.append(substr)
                    dfs(j + 1)
                    currRes.pop()
        dfs(0)
        return res


        # optimal
        # TC: O(n^3), SC: O(n^3)
        n = len(s)
        dp = {}    # i -> valid sentences from i till end
        hashset = set(wordDict)
        def dfs(i):
            if i == n:
                return [""]    # valid sentence
            if i in dp:
                return dp[i]
            currRes = []
            for j in range(i, n):
                substr = s[i:j+1]
                if substr not in hashset:
                    continue
                sentences = dfs(j + 1)
                for sentence in sentences:
                    if sentence:
                        currRes.append(substr + " " + sentence)
                    else:
                        currRes.append(substr)
            dp[i] = currRes
            return dp[i]
        return dfs(0)