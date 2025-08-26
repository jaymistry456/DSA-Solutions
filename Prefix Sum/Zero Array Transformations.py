# https://leetcode.com/problems/zero-array-transformation-ii/description/

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        # brute-force
        # TC: O(n*q), SC: O(1)
        n = len(nums)
        def helper():
            for num in nums:
                if num != 0:
                    return False
            return True
        if helper():
            return 0
        for i in range(len(queries)):
            start, end, val = queries[i]
            for j in range(start, end + 1):
                nums[j] = max(nums[j] - val, 0)
            if helper():
                return i + 1
        return -1


        # better
        # TC: O(n*q), SC: O(1)
        count = 0
        for num in nums:
            if num > 0:
                count += 1
        if count == 0:
            return 0
        for i in range(len(queries)):
            start, end, val = queries[i]
            for j in range(start, end + 1):
                before = nums[j]
                nums[j] = max(0, nums[j] - val)
                if before > 0 and nums[j] == 0:
                    count -= 1
            if count == 0:
                return i + 1
        return -1


        # optimal
        # TC: O((n+q)logq), SC: O(n)
        n = len(nums)
        if all(num == 0 for num in nums):
            return 0
        def helper(maxQ):
            diff = [0] * (n + 1)
            for start, end, val in queries[:maxQ+1]:
                diff[start] += val
                diff[end + 1] -= val
            curr = 0
            for i in range(len(nums)):
                curr += diff[i]
                if curr < nums[i]:
                    return False
            return True
        l = 0
        r = len(queries) - 1
        res = -1
        while l <= r:
            mid = l + (r - l) // 2
            if helper(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res + 1 if res != -1 else -1