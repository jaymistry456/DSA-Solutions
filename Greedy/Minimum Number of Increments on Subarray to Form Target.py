# https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/description/

class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        # brute-force
        # TC: O(n^max(target)), SC: O(n)
        res = 0
        n = len(target)
        arr = [0] * n
        while arr != target:
            i = 0
            while i < n:
                if arr[i] < target[i]:
                    j = i
                    while j < n and arr[j] < target[j]:
                        arr[j] += 1
                        j += 1
                    res += 1
                    i = j
                else:
                    i += 1
        return res


        # optimal
        # TC: O(n), SC: O(1)
        res = target[0]
        for i in range(1, len(target)):
            if target[i] > target[i - 1]:
                res += target[i] - target[i - 1]
        return res