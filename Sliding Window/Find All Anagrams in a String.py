# https://leetcode.com/problems/find-all-anagrams-in-a-string/

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # brute-force
        # TC: O(n1*n2), SC: O(1)
        n1 = len(s)
        n2 = len(p)
        hashmapP = [0] * 26
        res = []
        for i in range(n2):
            hashmapP[ord(p[i]) - ord('a')] += 1
        for i in range(n1 - n2 + 1):
            hashmapS = [0] * 26
            for j in range(i, i + n2):
                hashmapS[ord(s[j]) - ord('a')] += 1
            if hashmapS == hashmapP:
                res.append(i)
        return res


        # optimal
        # TC: O(n1), SC: O(1)
        n1 = len(s)
        n2 = len(p)
        if n1 < n2:
            return []
        res = []
        hashmapS = [0] * 26
        hashmapP = [0] * 26
        for i in range(n2):
            hashmapS[ord(s[i]) - ord('a')] += 1
            hashmapP[ord(p[i]) - ord('a')] += 1
        if hashmapS == hashmapP:
            res.append(0)
        for i in range(n2, n1):
            hashmapS[ord(s[i - n2]) - ord('a')] -= 1
            hashmapS[ord(s[i]) - ord('a')] += 1
            if hashmapS == hashmapP:
                res.append(i - n2 + 1)
        return res