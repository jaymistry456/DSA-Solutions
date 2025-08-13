# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # brute-force
        # TC: O(n^2), SC: O(1)
        n = len(weights)
        def isValid(maxCapacity):
            currDays = 1
            currWeight = 0
            for i in range(len(weights)):
                if currWeight + weights[i] <= maxCapacity:
                    currWeight += weights[i]
                else:
                    currDays += 1
                    currWeight = weights[i]
                    if currDays > days:
                        return False
            return True
        for currCapacity in range(max(weights), sum(weights) + 1):
            if isValid(currCapacity):
                return currCapacity


        # optimal
        # TC: O(nlogn), SC: O(1)
        def isValid(maxCapacity):
            currWeight = 0
            currDays = 1
            for i in range(len(weights)):
                if currWeight + weights[i] <= maxCapacity:
                    currWeight += weights[i]
                else:
                    currWeight = weights[i]
                    currDays += 1
                    if currDays > days:
                        return False
            return True
        l = max(weights)
        r = sum(weights)
        res = -1
        while l <= r:
            currCapacity = l + (r - l) // 2
            if isValid(currCapacity):
                res = currCapacity
                r = currCapacity - 1
            else:
                l = currCapacity + 1
        return res