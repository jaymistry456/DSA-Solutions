# https://leetcode.com/problems/product-of-array-except-self/description/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # TC: O(n), SC: O(n)
        n = len(nums)
        res = []
        curr = 1
        for i in range(n):
            curr *= nums[i]
            res.append(curr)  
        right = 1
        for i in range(n - 1, -1, -1):
            # left product
            left = 1
            if i - 1 >= 0:
                left = res[i - 1]
            # right product
            if i + 1 < n:
                right *= nums[i + 1]
            res[i] = left * right
        return res