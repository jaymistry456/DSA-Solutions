# https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # brute-force
        # TC: O(n^2), SC: O(1)
        n = len(nums)
        res = 0
        for i in range(n):
            currSum = 0
            for j in range(i, n):
                currSum += nums[j]
                if currSum == k:
                    res += 1
        return res


        # optimal
        # TC: O(n), SC: O(n)
        n = len(nums)
        hashmap = {}    # key (sum) -> value (no. of indexes with sum)
        hashmap[0] = 1
        currSum = 0
        res = 0
        for i in range(n):
            currSum += nums[i]
            if currSum - k in hashmap:
                res += hashmap[currSum - k]
            if currSum in hashmap:
                hashmap[currSum] += 1
            else:
                hashmap[currSum] = 1
        return res