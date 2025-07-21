# https://leetcode.com/problems/squares-of-a-sorted-array/description/

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # brute-force
        # TC: O(nlogn), SC: O(1)
        res = []
        for i in range(len(nums)):
            res.append(nums[i] ** 2)
        res.sort()
        return res


        # optimal
        # TC: O(n), SC: O(1)
        n = len(nums)
        res = [0] * n
        l = 0
        r = n - 1
        i = n - 1
        while l <= r:
            if nums[l] ** 2 >= nums[r] ** 2:
                res[i] = nums[l] ** 2
                l += 1
            else:
                res[i] = nums[r] ** 2
                r -= 1
            i -= 1
        return res