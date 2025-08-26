# https://leetcode.com/problems/palindromic-substrings/description/

class Solution:
    def countSubstrings(self, s: str) -> int:
        # brute-force
        # TC: O(n^2), SC: O(1)
        def helper(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        res = 0
        n = len(s)
        for i in range(n):
            for j in range(i, n):
                if helper(i, j):
                    res += 1
        return res


        # optimal
        # TC: O(n), SC: O(1)
        res = 0
        n = len(s)
        for i in range(n):
            # odd
            l = i
            r = i
            while l >= 0 and r < n and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            # even
            l = i
            r = i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
        return res