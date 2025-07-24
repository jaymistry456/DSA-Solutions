# https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # brute-force
        # TC: O(n^2), SC: O(n)
        n = len(nums)
        if sum(nums) % 2 == 1:
            return False
        def dfs(i, target):
            if target == 0:
                return True
            if target < 0 or i == n:
                return False
            # include or skip
            return dfs(i + 1, target - nums[i]) or dfs(i + 1, target)
        return dfs(0, sum(nums) // 2)


        # optimal
        # TC: O(n*target), SC: SC: O(n*target)
        n = len(nums)
        if sum(nums) % 2 == 1:
            return False
        dp = {} # key (i, currTarget) -> value (True or False)
        def dfs(i, target):
            if target == 0:
                return True
            if target < 0 or i == n:
                return False
            if (i, target) in dp:
                return dp[(i, target)]
            dp[(i, target)] = dfs(i + 1, target - nums[i]) or dfs(i + 1, target)
            return dp[(i, target)]
        return dfs(0, sum(nums) // 2)