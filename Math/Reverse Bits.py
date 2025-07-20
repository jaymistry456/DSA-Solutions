# https://leetcode.com/problems/reverse-bits/

class Solution:
    def reverseBits(self, n: int) -> int:
        # TC: O(logn), SC: O(1)
        res = 0
        for i in range(32):
            remainder = n % 2
            res = res * 2 + remainder
            n //= 2
        return res