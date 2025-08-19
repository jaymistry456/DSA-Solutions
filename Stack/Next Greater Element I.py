# https://leetcode.com/problems/next-greater-element-i/description/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # brute-force
        # TC: O(m*n + n^2), SC: O(n)
        m = len(nums1)
        n = len(nums2)
        nextGreater = [-1] * n
        for i in range(n):
            for j in range(i + 1, n):
                if nums2[j] > nums2[i]:
                    nextGreater[i] = nums2[j]
                    break
        res = []
        for i in range(m):
            for j in range(n):
                if nums1[i] == nums2[j]:
                    res.append(nextGreater[j])
        return res


        # optimal
        # TC: O(n), SC: O(n)
        m = len(nums1)
        n = len(nums2)
        nextGreater = [-1] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and stack[-1] <= nums2[i]:
                stack.pop()
            if stack:
                nextGreater[i] = stack[-1]
            stack.append(nums2[i])
        res = []
        hashmap = {}    # nums2[i] -> i
        for i in range(n):
            hashmap[nums2[i]] = i
        for i in range(m):
            index = hashmap[nums1[i]]
            res.append(nextGreater[index])
        return res