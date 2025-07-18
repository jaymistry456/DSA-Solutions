# https://leetcode.com/problems/longest-palindrome/description/

class Solution:
    def longestPalindrome(self, s: str) -> int:
        # brute-force
        # Try all subsets
        # TC: O(n*2^n), SC: O(n)


        # optimal using hashmap
        hashmap = defaultdict(int)  # key (char) -> val (freq starting at 0)
        res = 0
        for char in s:
            hashmap[char] += 1
            if hashmap[char] % 2 == 0:
                res += 2
        for char in hashmap:
            if hashmap[char] % 2 == 1:
                res += 1
                break
        return res