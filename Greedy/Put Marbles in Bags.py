# https://leetcode.com/problems/put-marbles-in-bags/

class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        # TC: O(nlogn), SC: O(n)
        arr = []
        for i in range(len(weights) - 1):
            arr.append(weights[i] + weights[i + 1])
        arr.sort()
        minScore = 0
        for i in range(k - 1):
            minScore += arr[i]
        maxScore = 0
        i = len(arr) - 1
        for _ in range(k - 1):
            maxScore += arr[i]
            i -= 1
        return maxScore - minScore