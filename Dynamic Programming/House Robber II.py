# https://leetcode.com/problems/house-robber-ii/

class Solution:
    def rob(self, nums: List[int]) -> int:
        # brute-force
        # TC: O(2^n), SC: O(n)
        if len(nums) <= 2:
            return max(nums)
        def houseRobber(houses):
            n = len(houses)
            def dfs(i):
                if i >= n:
                    return 0
                return max(houses[i] + dfs(i + 2), dfs(i + 1))
            return dfs(0)
        return max(houseRobber(nums[:-1]), houseRobber(nums[1:]))


        # optimal
        # TC: O(n^2), SC: O(n)
        if len(nums) <= 2:
            return max(nums)
        def houseRobber(houses):
            dp = {}    # i -> maxProfit from i to the end
            n = len(houses)
            def dfs(i):
                if i >= n:
                    return 0
                if i in dp:
                    return dp[i]
                dp[i] = max(houses[i] + dfs(i + 2), dfs(i + 1))
                return dp[i]
            return dfs(0)
        return max(houseRobber(nums[:-1]), houseRobber(nums[1:]))