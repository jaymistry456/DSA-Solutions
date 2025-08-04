# https://leetcode.ca/all/759.html

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

# TC: O(nlogn), SC: O(n)
def employeeFreeTime(schedule: List[List[Interval]]) -> List[Interval]:
    intervals = []
    for i in range(len(schedule)):
        employee = schedule[i]
        for j in range(len(employee)):
            intervals.append(employee[j])
    intervals.sort(key=lambda x:x.start)
    mergedIntervals = []
    prev = intervals[0]
    for i in range(1, len(intervals)):
        if intervals[i].start <= prev.end:
            prev.end = max(prev.end, intervals[i].end)
        else:
            mergedIntervals.append(prev)
            prev = intervals[i]
    mergedIntervals.append(prev)
    res = []
    for i in range(1, len(mergedIntervals)):
        prev = mergedIntervals[i - 1]
        curr = mergedIntervals[i]
        if prev.end < curr.start:
            res.append(Interval(prev.end, curr.start))
    return res