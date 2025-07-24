# https://leetcode.com/problems/container-with-most-water/description/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # brute-force
        # TC: O(n^2), SC: O(1)
        n = len(height)
        res = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                res = max(res, min(height[i], height[j]) * (j - i))
        return res


        # optimal
        # TC: O(n), SC: O(1)
        n = len(height)
        l = 0
        r = n - 1
        res = 0
        while l < r:
            res = max(res, min(height[l], height[r]) * (r - l))
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return res