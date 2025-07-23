# https://leetcode.com/problems/combination-sum/description/

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # TC: O(2^target), SC: O(target)
        n = len(candidates)
        currArr = []
        res = []
        def backtrack(target, i):
            if target == 0:
                res.append(currArr.copy())
                return
            if target < 0 or i == n:
                return
            # include
            currArr.append(candidates[i])
            backtrack(target - candidates[i], i)
            currArr.pop()
            # skip
            backtrack(target, i + 1)
        backtrack(target, 0)
        return res