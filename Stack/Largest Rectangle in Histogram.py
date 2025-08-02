# https://leetcode.com/problems/largest-rectangle-in-histogram/

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # brute-force
        # TC: O(n^2), SC: O(1)
        res = 0
        n = len(heights)
        for i in range(n):
            currMin = heights[i]
            for j in range(i, n):
                currMin = min(currMin, heights[j])
                res = max(res, currMin * (j - i + 1))
        return res


        # optimal
        # TC: O(n), SC: O(n)
        stack = []  # (prevIndex, prevHeight)
        n = len(heights)
        res = 0
        for i in range(n):
            start = i
            while stack and stack[-1][1] > heights[i]:
                prevIndex, prevHeight = stack.pop()
                res = max(res, (i - prevIndex) * prevHeight)
                start = prevIndex
            stack.append((start, heights[i]))
        while stack:
            prevIndex, prevHeight = stack.pop()
            res = max(res, (n - prevIndex) * prevHeight)
        return res