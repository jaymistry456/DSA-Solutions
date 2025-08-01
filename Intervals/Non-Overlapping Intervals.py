# https://leetcode.com/problems/non-overlapping-intervals/description/

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # TC: O(nlogn), SC: O(1)
        intervals.sort(key=lambda x:x[1])
        res = 0
        i = 1
        currEnd = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] < currEnd:
                res += 1
            else:
                currEnd = max(currEnd, intervals[i][1])
        return res