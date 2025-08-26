# https://leetcode.com/problems/permutation-in-string/description/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # brute-force
        # TC: O(n1*n2), SC: O(1)
        n1 = len(s1)
        n2 = len(s2)
        if n1 > n2:
            return False
        for i in range(n2 - n1 + 1):
            hash1 = defaultdict(int)    # char -> freq of char
            hash2 = defaultdict(int)    # char -> freq of char
            for j in range(n1):
                hash1[s1[j]] += 1
                hash2[s2[i + j]] += 1
            if hash1 == hash2:
                return True
        return False


        # brute-force
        # TC: O(n2), SC: O(1)
        n1 = len(s1)
        n2 = len(s2)
        if n1 > n2:
            return False
        hash1 = defaultdict(int)    # char -> freq of char
        hash2 = defaultdict(int)    # char -> freq of char
        for i in range(n1):
            hash1[s1[i]] += 1
            hash2[s2[i]] += 1
        if hash1 == hash2:
            return True
        for i in range(n1, n2):
            hash2[s2[i]] += 1
            hash2[s2[i - n1]] -= 1
            if hash2[s2[i - n1]] == 0:
                del hash2[s2[i - n1]]
            if hash1 == hash2:
                return True
        return False