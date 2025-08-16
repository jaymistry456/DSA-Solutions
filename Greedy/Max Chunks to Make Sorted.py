# https://leetcode.com/problems/max-chunks-to-make-sorted/description/

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        # brute-force
        # TC: O(n^2), SC: O(1)
        n = len(arr)
        res = 0
        for i in range(n):
            maxNum = float("-inf")
            for j in range(i+1):
                maxNum = max(maxNum, arr[j])
            if maxNum == i:
                res += 1
        return res


        # optimal
        # TC: O(n), SC: O(1)
        n = len(arr)
        maxNum = float("-inf")
        res = 0
        for i in range(n):
            maxNum = max(maxNum, arr[i])
            if maxNum == i:
                res += 1
        return res