# https://leetcode.com/problems/maximum-profit-in-job-scheduling/description/

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # brute-force
        # TC: O(2^n*n), SC: O(n)
        arr = sorted(zip(startTime, endTime, profit))
        def dfs(i):
            if i == len(arr):
                return 0
            # skip
            res = dfs(i + 1)
            # include
            next = -1
            for j in range(i + 1, len(arr)):
                if arr[j][0] >= arr[i][1]:
                    next = j
                    break
            if next != -1:
                res = max(res, arr[i][2] + dfs(j))
            else:
                res = max(res, arr[i][2])
            return res
        return dfs(0)


        # better
        # TC: O(n^2), SC: O(n)
        arr = sorted(zip(startTime, endTime, profit))
        dp = {} # key (time i) -> value (max profit from time i to end)
        def dfs(i):
            if i == len(arr):
                return 0
            if i in dp:
                return dp[i]
            # skip
            dp[i] = dfs(i + 1)
            # include
            next = -1
            for j in range(i + 1, len(arr)):
                if arr[j][0] >= arr[i][1]:
                    next = j
                    break
            if next != -1:
                dp[i] = max(dp[i], arr[i][2] + dfs(j))
            else:
                dp[i] = max(dp[i], arr[i][2])
            return dp[i]
        return dfs(0)


        # optimal
        # TC: O(nlogn), SC: O(n)
        arr = sorted(zip(startTime, endTime, profit))
        dp = {} # key (time i) -> value (max profit from time i till end)
        def dfs(i):
            if i == len(arr):
                return 0
            if i in dp:
                return dp[i]
            # skip
            dp[i] = dfs(i + 1)
            # include
            l = i + 1
            r = len(arr) - 1
            next = -1
            while l <= r:
                mid = l + (r - l) // 2
                if arr[mid][0] >= arr[i][1]:
                    next = mid
                    r = mid - 1
                else:
                    l = mid + 1
            if next != -1:
                dp[i] = max(dp[i], arr[i][2] + dfs(next))
            else:
                dp[i] = max(dp[i], arr[i][2])
            return dp[i]
        return dfs(0)