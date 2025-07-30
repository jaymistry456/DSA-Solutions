# https://leetcode.com/problems/reverse-integer/description/

class Solution:
    def reverse(self, x: int) -> int:
        # TC: O(logn), SC: O(1)
        sign = 1
        if x < 0:
            sign = -1
        else:
            sign = 1
        x = abs(x)
        res = 0
        while x > 0:
            remainder = x % 10
            x //= 10
            if res > (pow(2, 31) - 1 - remainder) // 10:
                return 0
            res = res * 10 + remainder
        return sign * res