# https://leetcode.com/problems/minimum-operations-to-make-array-equal-to-target/description/

class Solution:
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:
        # TC: O(n), SC: O(1)
        res = 0
        inc = 0
        dec = 0
        for i in range(len(nums)):
            currDiff = target[i] - nums[i]
            if currDiff < 0:
                if dec < abs(currDiff):
                    res += abs(currDiff) - dec
                dec = abs(currDiff)
                inc = 0
            elif currDiff > 0:
                if inc < abs(currDiff):
                    res += abs(currDiff) - inc
                inc = abs(currDiff)
                dec = 0
            else:
                inc = 0
                dec = 0
        return res