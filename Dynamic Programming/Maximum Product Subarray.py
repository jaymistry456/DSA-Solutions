# https://leetcode.com/problems/maximum-product-subarray/

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # brute-force
        # TC: O(n^2), SC: O(1)
        n = len(nums)
        res = max(nums)
        for i in range(n):
            curr = 1
            for j in range(i, n):
                curr *= nums[j]
                res = max(res, curr)
        return res


        # optimal
        # TC: O(n), SC: O(1)
        n = len(nums)
        res = max(nums)
        currMin = 1
        currMax = 1
        for i in range(n):
            temp = currMax
            currMax = max(currMax * nums[i], currMin * nums[i], nums[i])
            currMin = min(temp * nums[i], currMin * nums[i], nums[i])
            res = max(res, currMax)
        return res