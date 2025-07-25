# https://leetcode.com/problems/next-permutation/

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # brute-force
        # TC: O(n!*n), SC: O(n!*n)
        # generate all permuatations
        # sort them in lexicographical order
        # find the current permutation in the list
        # find the next permutation in the list


        # optimal
        # TC: O(n), SC: O(1)
        def reverseRange(i, j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        n = len(nums)
        # find the decreasing number
        index = -1
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                index = i
                break
        if index == -1:
            reverseRange(0, n - 1)
            return
        # find the number just greater than the decreasing number
        for i in range(n - 1, index, -1):
            if nums[i] > nums[index]:
                nums[i], nums[index] = nums[index], nums[i]
                break
        # reverse the suffix
        reverseRange(index + 1, n - 1)