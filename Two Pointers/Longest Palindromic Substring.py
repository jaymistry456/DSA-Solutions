# https://leetcode.com/problems/longest-palindromic-substring/description/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # brute-force
        # TC: O(n^3), SC: O(1)
        n = len(s)
        res = ''
        resLen = 0
        def isPalindrome(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        for i in range(n):
            for j in range(i, n):
                if isPalindrome(i, j):
                    if j - i + 1 > resLen:
                        resLen = j - i + 1
                        res = s[i:j+1]
        return res


        # optimal
        # TC: O(n^2), SC: O(1)
        n = len(s)
        resLen = 0
        resStart = -1
        resEnd = -1
        for i in range(n):
            # odd length
            l = i
            r = i
            while l >= 0 and r < n - 1 and s[l] == s[r]:
                if r - l + 1 > resLen:
                    resLen = r - 1 + 1
                    resStart = l
                    resEnd = r
                l -= 1
                r += 1
            # even length
            l = i
            r = i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 > resLen:
                    resLen = r - 1 + 1
                    resStart = l
                    resEnd = r
                l -= 1
                r += 1
        return s[resStart:resEnd+1]