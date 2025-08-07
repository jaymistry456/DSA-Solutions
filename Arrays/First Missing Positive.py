# https://leetcode.com/problems/first-missing-positive/

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # brute-force
        # TC: O(n^2), SC: O(1)
        n = len(nums)
        for i in range(1, n + 1):
            flag = False
            for j in range(n):
                if nums[j] == i:
                    flag = True
                    break
            if not flag:
                return i
        return n + 1


        # better
        # TC: O(n), SC: O(n)
        n = len(nums)
        hashset = set(nums)
        for i in range(1, n + 1):
            if i not in hashset:
                return i
        return n + 1


        # optimal
        # TC: O(n), SC: O(1)
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                correctIndex = nums[i] - 1
                nums[correctIndex], nums[i] = nums[i], nums[correctIndex]
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1