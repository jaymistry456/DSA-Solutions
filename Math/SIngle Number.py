# https://leetcode.com/problems/single-number/description/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # brute-force
        # TC: O(n^2), SC: O(1)
        for i in range(len(nums)):
            is_unique = True
            for j in range(len(nums)):
                if i != j and nums[i] == nums[j]:
                    is_unique = False
                    break
            if is_unique:
                return nums[i]


        # better
        # TC: O(n), SC: O(n)
        hashmap = {}    # key (number) -> value (frequency)
        for i in range(len(nums)):
            if nums[i] in hashmap:
                hashmap[nums[i]] += 1
            else:
                hashmap[nums[i]] = 1
        for number, freq in hashmap.items():
            if freq == 1:
                return number

        
        # optimal
        # TC: O(n), SC: O(1)
        res = 0
        for i in range(len(nums)):
            res ^= nums[i]
        return res