# https://leetcode.com/problems/combination-sum-iv/description/

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # brute-force
        # TC: O(target^n), SC: O(target)
        def backtrack(currSum):
            if currSum == target:
                return 1
            if currSum > target:
                return 0
            res = 0
            for i in range(len(nums)):
                res += backtrack(currSum + nums[i])
            return res
        return backtrack(0)


        # optimal
        # TC: O(target*n), SC: O(target)
        dp = {} # key (currSum) -> value (no. of ways to form currSum)
        def backtrack(currSum):
            if currSum == target:
                return 1
            if currSum > target:
                return 0
            if currSum in dp:
                return dp[currSum]
            dp[currSum] = 0
            for i in range(len(nums)):
                dp[currSum] += backtrack(currSum + nums[i])
            return dp[currSum]
        return backtrack(0)