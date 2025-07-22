# https://leetcode.com/problems/3sum/description/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # brute-force
        # TC: O(n^3), SC: O(n)
        n = len(nums)
        nums.sort()
        res = set()
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        res.add(tuple([nums[i], nums[j], nums[k]]))
        return [list(i) for i in res]


        # optimal
        # TC: O(n^2), SC: O(n)
        n = len(nums)
        nums.sort()
        res = []
        i = 0
        while i < n - 2:
            j = i + 1
            k = n - 1
            while j < k:
                currSum = nums[i] + nums[j] + nums[k]
                if currSum == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                elif currSum < 0:
                    j += 1
                else:
                    k -= 1
            i += 1
            while i < n - 2 and nums[i] == nums[i - 1]:
                i += 1
        return res