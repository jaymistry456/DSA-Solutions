# https://leetcode.com/problems/plates-between-candles/description/

class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        # TC: O(n + q), SC: O(n)
        n = len(s)
        plates = [0] * n
        curr = 0
        for i in range(n):
            if s[i] == "*":
                curr += 1
            plates[i] = curr
        leftCandle = [-1] * n
        curr = -1
        for i in range(n):
            if s[i] =="|":
                curr = i
            leftCandle[i] = curr
        rightCandle = [-1] * n
        curr = -1
        for i in range(n - 1, -1, -1):
            if s[i] == "|":
                curr = i
            rightCandle[i] = curr
        q = len(queries)
        res = [0] * q
        for i in range(len(queries)):
            start, end = queries[i]
            leftIndexOfCandle = rightCandle[start]
            rightIndexOfCandle = leftCandle[end]
            if leftIndexOfCandle != -1 and rightIndexOfCandle != -1 and leftIndexOfCandle < rightIndexOfCandle:
                res[i] = plates[rightIndexOfCandle] - plates[leftIndexOfCandle]
        return res