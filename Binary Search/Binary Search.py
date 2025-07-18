# https://leetcode.com/problems/binary-search/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # # iterative
        # # TC: O(logn), SC: O(1)
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1

        # recursive
        # TC: O(logn), SC: O(1)
        def recursive(l, r):
            if l <= r:
                mid = l + (r - l) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    return recursive(mid + 1, r)
                else:
                    return recursive(l, mid - 1)
            return -1
        return recursive(0, len(nums) - 1)