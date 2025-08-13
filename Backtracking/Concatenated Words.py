# https://leetcode.com/problems/concatenated-words/description/

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        # brute-force
        # TC: O(2^l*m), SC: O(m*l)
        hashset = set(words)
        res = set()
        currRes = []
        def dfs(i, currWord):
            if i == len(currWord):
                res.add("".join(currRes))
                return
            for j in range(i, len(currWord)):
                substr = currWord[i:j+1]
                if substr in hashset:
                    currRes.append(substr)
                    dfs(j + 1, currWord)
                    currRes.pop()
        for word in hashset:
            hashset.remove(word)
            dfs(0, word)
            hashset.add(word)
        return list(res)


        # optimal
        # TC: O(m*l^2), SC: O(m*l)
        hashset = set(words)
        dp = {}    # word -> True or False
        def dfs(word):
            if word in dp:
                return dp[word]
            for i in range(len(word)):
                if word[:i+1] in hashset and (word[i+1:] in hashset or dfs(word[i+1:])):
                    dp[word] = True
                    return True
            dp[word] = False
            return False
        res = []
        for word in words:
            if dfs(word):
                res.append(word)
        return res