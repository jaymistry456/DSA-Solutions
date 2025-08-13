# https://leetcode.com/problems/contiguous-array/

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # brute-force
        # TC: O(n^2), SC: O(1)
        res = 0
        for i in range(len(nums)):
            curr = 0
            for j in range(i, len(nums)):
                if nums[j] == 0:
                    curr -= 1
                else:
                    curr += 1
                if curr == 0:
                    res = max(res, j - i + 1)
        return res


        # optimal
        # TC: O(n), SC: O(n)
        hashmap = {}    # index -> first index of curr diff of 0 and 1
        hashmap[0] = -1
        curr = 0
        res = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                curr -= 1
            else:
                curr += 1
            if curr in hashmap:
                res = max(res, i - hashmap[curr])
            else:
                hashmap[curr] = i
        return res