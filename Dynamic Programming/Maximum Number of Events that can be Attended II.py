# https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii/description/

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        # brute-force
        # TC: O(2^n*n), SC: O(n)
        events.sort(key=lambda x:x[0])
        n = len(events)
        def dfs(i, currK):
            if i == n or currK == k:
                return 0
            # skip
            res = dfs(i + 1, currK)
            # include
            next = -1
            for j in range(i + 1, n):
                if events[j][0] > events[i][1]:
                    next = j
                    break
            if next != -1:
                res = max(res, events[i][2] + dfs(next, currK + 1))
            else:
                res = max(res, events[i][2])
            return res
        return dfs(0, 0)


        # better
        # TC: O(n^2), SC: O(n)
        events.sort(key=lambda x:x[0])
        n = len(events)
        dp = {} # key (time i, currK) -> value (max profit from time i to end)
        def dfs(i, currK):
            if i == n or currK == k:
                return 0
            if (i, currK) in dp:
                return dp[(i, currK)]
            # skip
            dp[(i, currK)] = dfs(i + 1, currK)
            # include
            next = -1
            for j in range(i + 1, n):
                if events[j][0] > events[i][1]:
                    next = j
                    break
            if next != -1:
                dp[(i, currK)] = max(dp[(i, currK)], events[i][2] + dfs(next, currK + 1))
            else:
                dp[(i, currK)] = max(dp[(i, currK)], events[i][2])
            return dp[(i, currK)]
        return dfs(0, 0)


        # optimal
        # TC: O(nlogn), SC: O(n)
        events.sort(key=lambda x:x[0])
        n = len(events)
        dp = {} # key (time i, currK) -> value (max profit from i to end)
        def dfs(i, currK):
            if i == n or currK == k:
                return 0
            if (i, currK) in dp:
                return dp[(i, currK)]
            # skip
            dp[(i, currK)] = dfs(i + 1, currK)
            # include
            next = -1
            l = i + 1
            r = n - 1
            while l <= r:
                mid = l + (r - l) // 2
                if events[mid][0] > events[i][1]:
                    next = mid
                    r = mid - 1
                else:
                    l = mid + 1
            if next != -1:
                dp[(i, currK)] = max(dp[(i, currK)], events[i][2] + dfs(next, currK + 1))
            else:
                dp[(i, currK)] = max(dp[(i, currK)], events[i][2])
            return dp[(i, currK)]
        return dfs(0, 0)