# https://neetcode.io/problems/meeting-schedule-ii

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # TC: O(nlogn), SC: O(n)
        events = [] # [time, eventType] where event Type is 1 for start, -1 for end
        for i in range(len(intervals)):
            events.append([intervals[i].start, 1])
            events.append([intervals[i].end, -1])
        events.sort()
        res = 0
        curr = 0
        for i in range(len(events)):
            curr += events[i][1]
            res = max(res, curr)
        return res