# https://leetcode.com/problems/sort-colors/description/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # brute-force
        # TC: O(nlogn), SC: O(1)
        nums.sort()
        return nums


        # better
        # TC: O(n), SC: O(1)
        n = len(nums)
        count = [0] * 3
        for i in range(n):
            count[nums[i]] += 1
        index = 0
        for i in range(3):
            while count[i]:
                nums[index] = i
                count[i] -= 1
                index += 1


        # optimal
        # TC: O(n), SC: O(1)
        n = len(nums)
        l, mid, r = 0, 0, n - 1
        while mid <= r:
            if nums[mid] == 0:
                nums[l], nums[mid] = nums[mid], nums[l]
                l += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[r], nums[mid] = nums[mid], nums[r]
                r -= 1