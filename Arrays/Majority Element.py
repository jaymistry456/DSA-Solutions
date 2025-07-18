# https://leetcode.com/problems/majority-element/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # brute-force
        # TC: O(n), SC: O(n)
        hashmap = {}    # key (number) -> val (frequency)
        for n in nums:
            if n in hashmap:
                hashmap[n] += 1
            else:
                hashmap[n] = 1
        for key, val in hashmap.items():
            if val > len(nums) // 2:
                return key


        # optimal
        # TC: O(n), SC: O(1)
        res = None
        count = 0
        for n in nums:
            if count == 0:
                res = n
            if res == n:
                count += 1
            else:
                count -= 1
        return res