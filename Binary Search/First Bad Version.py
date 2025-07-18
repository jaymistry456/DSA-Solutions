# https://leetcode.com/problems/first-bad-version/description/

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # brute-force
        # TC: O(n), SC: O(1)
        for x in range(1, n + 1):
            if isBadVersion(x):
                return x


        # optimal
        # TC: O(logn), SC: O(1)
        l = 1
        r = n
        while l < r:
            mid = l + (r - l) // 2
            if isBadVersion(mid):
                r = mid
            else:
                l = mid + 1
        return r