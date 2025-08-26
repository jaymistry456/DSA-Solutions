# https://leetcode.com/problems/target-sum/description/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # brute-force
        # TC: O(2^n), SC: O(n)
        n = len(nums)
        def dfs(i, currSum):
            if i == n:
                if currSum == target:
                    return 1
                return 0
            return dfs(i + 1, currSum + nums[i]) + dfs(i + 1, currSum - nums[i])
        return dfs(0, 0)


        # optimal
        # TC: O(n^2), SC: O(n^2)
        n = len(nums)
        dp = {}    # (i, currSum) -> no. way to build target sum expression
        def dfs(i, currSum):
            if i == n:
                if currSum == target:
                    return 1
                return 0
            if (i, currSum) in dp:
                return dp[(i, currSum)]
            dp[(i, currSum)] = dfs(i + 1, currSum + nums[i]) + dfs(i + 1, currSum - nums[i])
            return dp[(i, currSum)]
        return dfs(0, 0)