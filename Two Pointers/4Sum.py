# https://leetcode.com/problems/4sum/

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # brute-force
        # TC: O(n^4), SC: O(1)
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                for k in range(j + 1, n):
                    if k > j + 1 and nums[k] == nums[k - 1]:
                        continue
                    for l in range(k + 1, n):
                        if l > k + 1 and nums[l] == nums[l - 1]:
                            continue
                        currSum = nums[i] + nums[j] + nums[k] + nums[l]
                        if currSum == target:
                            res.append([nums[i], nums[j], nums[k], nums[l]])
        return res


        # optimal
        # TC: O(n^3), SC: O(1)
        n = len(nums)
        nums.sort()
        res = []
        i = 0
        while i < n - 3:
            j = i + 1
            while j < n - 2:
                l = j + 1
                r = n - 1
                while l < r:
                    currSum = nums[i] + nums[j] + nums[l] + nums[r]
                    if currSum == target:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        r -= 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
                    elif currSum < target:
                        l += 1
                    else:
                        r -= 1
                j += 1
                while j < n - 2 and nums[j] == nums[j - 1]:
                    j += 1
            i += 1
            while i < n - 3 and nums[i] == nums[i - 1]:
                i += 1
        return res