# https://leetcode.com/problems/powx-n/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        # brute-force
        # TC: O(n), SC: O(1)
        if x == 0:
            return 0
        if n == 0:
            return 1
        res = 1
        for _ in range(abs(n)):
            res *= x
        if n < 0:
            return 1 / res
        else:
            return res


        # optimal
        # TC: O(logn), SC: O(1)
        def recursive(x, n):
            if x == 0:
                return 0
            if n == 0:
                return 1
            res = recursive(x, n // 2)
            if n % 2 == 1:
                return res * res * x
            else:
                return res * res
        res = recursive(x, abs(n))
        if n < 0:
            return 1 / res
        else:
            return res