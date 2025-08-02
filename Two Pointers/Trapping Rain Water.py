# https://leetcode.com/problems/trapping-rain-water/description/

class Solution:
    def trap(self, height: List[int]) -> int:
        # brute-force
        # TC: O(n^2), SC: O(1)
        res = 0
        n = len(height)
        for i in range(n):
            leftMax = 0
            for j in range(i + 1):
                leftMax = max(leftMax, height[j])
            rightMax = 0
            for j in range(i, n):
                rightMax = max(rightMax, height[j])
            res += min(leftMax, rightMax) - height[i]
        return res


        # optimal using 2 arrays
        # TC: O(n), SC: O(n)
        n = len(height)
        res = 0
        leftMax = [0] * n
        leftMax[0] = height[0]
        for i in range(1, n):
            leftMax[i] = max(leftMax[i - 1], height[i])
        rightMax = [0] * n
        rightMax[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], height[i])
        res = 0
        for i in range(1, n - 1):
            res += min(leftMax[i], rightMax[i]) - height[i]
        return res


        # optimal using 1 array
        # TC: O(n), SC: O(n)
        n = len(height)
        leftMax = [0] * n
        leftMax[0] = height[0]
        for i in range(1, n):
            leftMax[i] = max(leftMax[i - 1], height[i])
        rightMax = height[n - 1]
        res = 0
        for i in range(n - 2, 0, -1):
            rightMax = max(rightMax, height[i])
            res += min(leftMax[i], rightMax) - height[i]
        return res