# https://leetcode.com/problems/3sum-closest/

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # brute-force
        # TC: O(n^3), SC: O(1)
        res = float('inf')
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    currSum = nums[i] + nums[j] + nums[k]
                    if abs(currSum - target) < abs(res - target):
                        res = currSum
        return res


        # optimal
        # TC: O(n^2), SC: O(1)
        nums.sort()
        i = 0
        n = len(nums)
        res = float('inf')
        while i < n - 2:
            l = i + 1
            r = n - 1
            while l < r:
                currSum = nums[i] + nums[l] + nums[r]
                if currSum == target:
                    return target
                elif currSum < target:
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                else:
                    r -= 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                if abs(currSum - target) < abs(res - target):
                    res = currSum
            i += 1
            while i < n - 2 and nums[i] == nums[i - 1]:
                i += 1
        return res