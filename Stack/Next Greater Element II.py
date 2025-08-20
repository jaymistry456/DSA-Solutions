# https://leetcode.com/problems/next-greater-element-ii/description/

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # brute-force
        # TC: O(n^2), SC: O(1)
        n = len(nums)
        res = [-1] * n
        for i in range(n):
            for j in range(i + 1, i + n):
                if nums[j % n] > nums[i]:
                    res[i] = nums[j % n]
                    break
        return res


        # better
        # TC: O(n), SC: O(n)
        n = len(nums)
        nums = nums + nums
        res = [-1] * n
        for i in range(len(nums) // 2):
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    res[i] = nums[j % n]
                    break
        return res


        # optimal
        # TC: O(n), SC: O(n)
        n = len(nums)
        res = [-1] * n
        stack = []
        for i in range(2 * n - 1, -1, -1):
            while stack and stack[-1] <= nums[i % n]:
                stack.pop()
            if i < n:
                if stack:
                    res[i] = stack[-1]
            stack.append(nums[i % n])
        return res