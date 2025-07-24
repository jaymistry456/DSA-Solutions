# https://leetcode.com/problems/subsets/description/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # TC: O(2^n), SC: O(n)
        n = len(nums)
        res = []
        currArr = []
        def backtrack(i):
            if i == n:
                res.append(currArr.copy())
                return
            # include
            currArr.append(nums[i])
            backtrack(i + 1)
            currArr.pop()
            # skip
            backtrack(i + 1)
        backtrack(0)
        return res