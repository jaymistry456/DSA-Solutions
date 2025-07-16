# https://leetcode.com/problems/valid-anagram/description/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # brute-force
        # TC: O(mlogm+nlogn), SC: O(n+m)
        return sorted(s) == sorted(t)

        # optimal using array
        # TC: O(m+n), SC:O(m+n)
        hashArray = [0] * 26
        for c in s:
            hashArray[ord(c) - ord('a')] += 1
        for c in t:
            hashArray[ord(c) - ord('a')] -= 1

        for i in range(len(hashArray)):
            if hashArray[i] != 0:
                return False
        return True

        # optimal using hashmap
        # TC: O(m+n), SC: O(m+n)
        hashmap = {}    # key -> character, val -> frequency
        # iterate over s
        for i in range(len(s)):
            key = s[i]
            if key in hashmap:
                hashmap[key] += 1
            else:
                hashmap[key] = 1
        # iterate over t
        for i in range(len(t)):
            key = t[i]
            if key not in hashmap:
                return False
            else:
                hashmap[key] -= 1
                if hashmap[key] == 0:
                    del hashmap[key]
        return len(hashmap) == 0