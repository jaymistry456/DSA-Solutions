# https://neetcode.io/problems/string-encode-and-decode

class Solution:

    # TC: O(n), SC: O(n)
    def encode(self, strs: List[str]) -> str:
        res = ''
        for i in range(len(strs)):
            res += str(len(strs[i])) + '#' + strs[i]
        return res

    # TC: O(n), SC: O(n)
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            length = ''
            while i < len(s) and ord('0') <= ord(s[i]) <= ord('9'):
                length += s[i]
                i += 1
            length = int(length)
            i += 1  # skip the '#' character
            res.append(s[i:i+length])
            i += length
        return res