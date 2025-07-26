# https://leetcode.com/problems/find-the-duplicate-number/

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # brute-force
        # TC: O(n^2), SC: O(1)
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    return nums[i]
        

        # optimal
        # TC: O(n), SC: O(n)
        n = len(nums)
        hashset = set()
        for i in range(n):
            if nums[i] in hashset:
                return nums[i]
            hashset.add(nums[i])