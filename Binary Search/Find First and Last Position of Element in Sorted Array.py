# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # brute-force
        # TC: O(n), SC: O(1)
        n = len(nums)
        res = [-1, -1]
        for i in range(n):
            if nums[i] == target:
                res[0] = i
                break
        for i in range(n - 1, -1, -1):
            if nums[i] == target:
                res[1] = i
                break
        return res


        # optimal
        # TC: O(logn), SC: O(1)
        n = len(nums)
        res = [-1, -1]
        l = 0
        r = n - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                res[0] = mid
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        l = 0
        r = n - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                res[1] = mid
                l = mid + 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return res