# https://leetcode.com/problems/split-array-largest-sum/description/

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # brute-force
        # TC: O(n^2), SC: O(1)
        n = len(nums)
        def isPossible(maxSum):
            currSum = 0
            currK = 1
            for i in range(len(nums)):
                if currSum + nums[i] > maxSum:
                    currSum = nums[i]
                    currK += 1
                else:
                    currSum += nums[i]
                if currK > k:
                    return False
            return True
        l = max(nums)
        r = sum(nums)
        res = float("inf")
        for maxSum in range(l, r + 1):
            if isPossible(maxSum):
                return maxSum


        # optimal
        # TC: O(nlogn), SC: O(1)
        n = len(nums)
        def isPossible(maxSum):
            currSum = 0
            currK = 1
            for i in range(len(nums)):
                if currSum + nums[i] > maxSum:
                    currSum = nums[i]
                    currK += 1
                else:
                    currSum += nums[i]
                if currK > k:
                    return False
            return True
        l = max(nums)
        r = sum(nums)
        res = float("inf")
        while l <= r:
            mid = l + (r - l) // 2
            if isPossible(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res