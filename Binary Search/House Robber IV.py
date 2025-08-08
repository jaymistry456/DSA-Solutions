# https://leetcode.com/problems/house-robber-iv/description/

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        # brute-force
        # TC: O(2^n), SC: O(n)
        n = len(nums)
        def dfs(i, currK):
            if currK == k:
                return 0
            if i >= n:
                return float("inf")
            return min(dfs(i + 1, currK), max(nums[i], dfs(i + 2, currK + 1)))
        return dfs(0, 0)


        # better
        # TC: O(n*k), SC: O(n*k)
        n = len(nums)
        dp = {}    # (i, currK) -> min capabilty from i till end
        def dfs(i, currK):
            if currK == k:
                return 0
            if i >= n:
                return float("inf")
            if (i, currK) in dp:
                return dp[(i, currK)]
            dp[(i, currK)] = min(dfs(i + 1, currK), max(nums[i], dfs(i + 2, currK + 1)))
            return dp[(i, currK)]
        return dfs(0, 0)


        # optimal
        # TC: O(nlogn), SC: O(1)
        n = len(nums)
        def isValid(currCapability):
            i = 0
            currK = 0
            while i < n:
                if nums[i] <= currCapability:
                    currK += 1
                    if currK == k:
                        return True
                    i += 2
                else:
                    i += 1
            return False
        l = min(nums)
        r = max(nums)
        res = float("inf")
        while l <= r:
            mid = l + (r - l) // 2
            if isValid(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res