# https://leetcode.com/problems/permutations/description/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # TC: O(n!*n), SC: O(n)
        n = len(nums)
        currArr = []
        res = []
        def backtrack():
            if len(currArr) == n:
                res.append(currArr.copy())
                return
            for i in range(n):
                if nums[i] not in currArr:
                    currArr.append(nums[i])
                    backtrack()
                    currArr.pop()
        backtrack()
        return res