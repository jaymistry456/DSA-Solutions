# https://leetcode.com/problems/merge-intervals/description/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # TC: O(nlogn), SC: O(1)
        n = len(intervals)
        intervals.sort()
        res = []
        i = 0
        while i < n:
            newInterval = intervals[i]
            while i + 1 < n and intervals[i + 1][0] <= newInterval[1]:
                newInterval[1] = max(newInterval[1], intervals[i + 1][1])
                i += 1
            res.append(newInterval)
            i += 1
        return res