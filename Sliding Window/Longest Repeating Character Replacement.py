# https://leetcode.com/problems/longest-repeating-character-replacement/description/

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # brute-force
        # TC: O(n^2), SC: O(1)
        n = len(s)
        res = 0
        for i in range(n):
            freq = [0] * 26
            maxFreq = 0
            for j in range(i, n):
                freq[ord(s[j]) - ord('A')] += 1
                maxFreq = max(maxFreq, freq[ord(s[j]) - ord('A')])
                if (j - i + 1) - maxFreq <= k:
                    res = max(res, j - i + 1)
        return res


        # optimal
        # TC: O(n), SC: O(1)
        n = len(s)
        l = 0
        r = 0
        freq = [0] * 26
        res = 0
        while r < n:
            freq[ord(s[r]) - ord('A')] += 1
            while (r - l + 1) - max(freq) > k:
                freq[ord(s[l]) - ord('A')] -= 1
                l += 1
            res = max(res, r - l + 1)
            r += 1
        return res