# https://leetcode.com/problems/largest-number/

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # TC: O(nlogn), SC: O(n)
        def compare(a, b):
            # -1 -> a comes before b
            # 1 -> b comes before a
            # 0 -> both are equal
            if a + b > b + a:
                return -1
            elif a + b < b + a:
                return 1
            else:
                return 0
        for i in range(len(nums)):
            nums[i] = str(nums[i])
        nums.sort(key=cmp_to_key(compare))
        return str(int(''.join(nums)))