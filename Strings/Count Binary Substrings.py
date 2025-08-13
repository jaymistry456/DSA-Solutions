# https://leetcode.com/problems/count-binary-substrings/description/

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        # TC: O(n), SC: O(1)
        res = 0
        prev = 0
        curr = 0
        n = len(s)
        i = 0
        while i < n:
            char = s[i]
            while i < n and s[i] == char:
                curr += 1
                i += 1
            res += min(prev, curr)
            prev = curr
            curr = 0
        return res