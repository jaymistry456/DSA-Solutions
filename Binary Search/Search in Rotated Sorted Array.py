# https://leetcode.com/problems/search-in-rotated-sorted-array/description/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # TC: O(logn), SC: O(1)
        def binarySearch(l, r):
            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return  - 1
        # find the starting position
        n = len(nums)
        l = 0
        r = n - 1
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] <= nums[r]:
                r = mid
            else:
                l = mid + 1
        if target > nums[-1]:
            return binarySearch(0, (l - 1) % n)
        else:
            return binarySearch(l, n - 1)