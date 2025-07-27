# https://leetcode.com/problems/rotate-array/description/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # brute-force
        # TC: O(n), SC: O(n)
        n = len(nums)
        res = [0] * n
        for i in range(n):
            res[(i + k) % n] = nums[i]
        for i in range(n):
            nums[i] = res[i]


        # optimal
        # TC: O(n), SC: O(1)
        n = len(nums)
        def reverseArr(l, r):
            while l < r:
                temp = nums[l]
                nums[l] = nums[r]
                nums[r] = temp
                l += 1
                r -= 1
        k %= n
        reverseArr(0, n - 1)
        reverseArr(0, k - 1)
        reverseArr(k, n - 1)