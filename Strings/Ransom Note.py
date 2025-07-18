# https://leetcode.com/problems/ransom-note/

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # brute-force
        # TC: O(m*n), SC: O(m)
        magazine = list(magazine)
        for char in ransomNote:
            if char in magazine:
                magazine.remove(char)
            else:
                return False
        return True


        # optimal using hashmap
        # TC: O(m+n), SC: O(1)
        hashmap = {}    # key (char) -> val (frequency)
        for char in magazine:
            if char in hashmap:
                hashmap[char] += 1
            else:
                hashmap[char] = 1
        for char in ransomNote:
            if char in hashmap:
                hashmap[char] -= 1
                if hashmap[char] == 0:
                    del hashmap[char]
            else:
                return False
        return True


        # optimal using array
        # TC: O(m+n), SC: O(1)
        arr = [0] * 26
        for char in magazine:
            arr[ord(char) - ord('a')] += 1
        for char in ransomNote:
            if arr[ord(char) - ord('a')] > 0:
                arr[ord(char) - ord('a')] -= 1
            else:
                return False
        return True