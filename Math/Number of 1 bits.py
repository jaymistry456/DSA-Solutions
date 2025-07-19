# https://leetcode.com/problems/number-of-1-bits/description/

class Solution:
    def hammingWeight(self, n: int) -> int:
        # TC: O(logn), SC: O(1)
        res = 0
        while n > 0:
            res += n % 2
            n //= 2
        return res