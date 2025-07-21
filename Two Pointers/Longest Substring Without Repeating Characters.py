# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # brute-force
        # TC: O(n^2), SC: O(n)
        n = len(s)
        res = 0
        for i in range(n):
            hashset = set()
            for j in range(i, n):
                if s[j] in hashset:
                    break
                hashset.add(s[j])
            res = max(res, len(hashset))
        return res


        # optimal
        # TC: O(n), SC: O(n)
        n = len(s)
        l = 0
        r = 0
        res = 0
        hashset = set()
        while r < n:
            while r < n and s[r] in hashset:
                hashset.remove(s[l])
                l += 1
            hashset.add(s[r])
            res = max(res, r - l + 1)
            r += 1
        return res