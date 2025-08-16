# https://leetcode.com/problems/isomorphic-strings/description/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # TC: O(n), SC: O(1)
        if len(s) != len(t):
            return False
        hashmap1 = {}    # s char -> t char
        hashmap2 = {}    # t char -> s char
        for i in range(len(s)):
            char1 = s[i]
            char2 = t[i]
            if char1 not in hashmap1 and char2 not in hashmap2:
                hashmap1[char1] = char2
                hashmap2[char2] = char1
            elif char1 not in hashmap1 or char2 not in hashmap2:
                return False
            else:
                if hashmap1[char1] != char2 or hashmap2[char2] != char1:
                    return False
        return True