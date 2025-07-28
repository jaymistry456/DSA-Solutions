# https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # brute-force
        # TC: O(2^n), SC: O(n)
        n = len(nums)
        def backtrack(i):
            if i == n - 1:
                return True
            for j in range(i + 1, i + nums[i] + 1):
                if backtrack(j):
                    return True
            return False
        return backtrack(0)


        # better
        # TC: O(n^2), SC: O(n)
        n = len(nums)
        dp = {} # key (i) -> value (True or False)
        def backtrack(i):
            if i == n - 1:
                return True
            if i in dp:
                return dp[i]
            for j in range(i + 1, i + nums[i] + 1):
                if backtrack(j):
                    dp[i] = True
                    return True
            dp[i] = False
            return False
        return backtrack(0)


        # optimal
        # TC: O(n), SC: O(1)
        n = len(nums)
        target = n - 1
        for i in range(n - 1, -1, -1):
            if i + nums[i] >= target:
                target = i
        return target == 0