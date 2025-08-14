# https://leetcode.com/problems/find-peak-element/

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # brute-force
        # TC: O(n), SC: O(1)
        if len(nums) == 1:
            return 0
        for i in range(len(nums)):
            if i == 0:
                if nums[i] > nums[i + 1]:
                    return i
            elif i == len(nums) - 1:
                if nums[i] > nums[i - 1]:
                    return i
            else:
                if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                    return i


        # optimal
        # TC: O(logn), SC: O(1)
        n = len(nums)
        l = 0
        r = n - 1
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] <= nums[mid + 1]:
                l = mid + 1
            else:
                r = mid
        return l