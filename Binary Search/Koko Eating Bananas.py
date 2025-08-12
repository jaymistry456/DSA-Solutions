# https://leetcode.com/problems/koko-eating-bananas/description/

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # brute-force
        # TC: O(n*max), SC: O(1)
        def isValid(currK):
            currHours = 0
            for i in range(len(piles)):
                currHours += math.ceil(piles[i] / currK)
                if currHours > h:
                    return False
            return True
        l = 1
        r = max(piles)
        for k in range(l, r + 1):
            if isValid(k):
                return k


        # optimal
        # TC: O(n*logmax), SC: O(1)
        def isValid(currK):
            currH = 0
            for i in range(len(piles)):
                currH += math.ceil(piles[i] / currK)
                if currH > h:
                    return False
            return True
        l = 1
        r = max(piles)
        res = -1
        while l <= r:
            mid = l + (r - l) // 2
            if isValid(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res