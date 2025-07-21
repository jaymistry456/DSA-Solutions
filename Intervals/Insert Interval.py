# https://leetcode.com/problems/insert-interval/

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # TC: O(n), SC: O(1)
        n = len(intervals)
        intervals.sort()
        res = []
        i = 0
        # all intervals before newInterval
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
        # all intervals between newInterval
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        res.append(newInterval)
        # all intervals after newInterval
        while i < len(intervals):
            res.append(intervals[i])
            i += 1
        return res