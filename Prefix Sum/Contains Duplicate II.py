# https://leetcode.com/problems/contains-duplicate-ii/

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # brute-force
        # TC: O(n^2), SC: O(1)
        for i in range(len(nums)):
            for j in range(i + 1, i + k + 1):
                if j < len(nums):
                    if nums[j] == nums[i]:
                        return True
        return False


        # optimal
        # TC: O(n), SC: O(n)
        hashmap = {}    # num -> index of num
        for i in range(len(nums)):
            if nums[i] in hashmap:
                if i - hashmap[nums[i]] <= k:
                    return True
            hashmap[nums[i]] = i
        return False
