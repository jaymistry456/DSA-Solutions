# https://neetcode.io/problems/meeting-schedule?list=neetcode150

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # brute-force
        # TC: O(n^2), SC: O(1)
        for i in range(len(intervals)):
            for j in range(i + 1, len(intervals)):
                if min(intervals[i].end, intervals[j].end) > max(intervals[i].start, intervals[j].start):
                    return False
        return True


        # optimal
        # TC: O(nlogn), SC: O(1)
        intervals.sort(key = lambda x:x.start) # sort by start times
        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[i - 1].end:
                return False
        return True