# https://leetcode.com/problems/word-pattern/description/

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # TC: O(n), SC: O(n)
        hashmap1 = {}    # word -> index
        hashmap2 = {}    # char -> index
        words = s.split()
        if len(pattern) != len(words):
            return False
        n = len(words)
        for i in range(n):
            if pattern[i] not in hashmap1 and words[i] not in hashmap2:
                hashmap1[pattern[i]] = hashmap2[words[i]] = i
            elif pattern[i] not in hashmap1 or words[i] not in hashmap2:
                return False
            else:
                if hashmap1[pattern[i]] != hashmap2[words[i]]:
                    return False
        return True