# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # TC: O(nlogn), SC: O(1)
        points.sort(key=lambda x:x[1])
        prevEnd = points[0][1]
        res = 1
        for start, end in points[1:]:
            if prevEnd < start:
                res += 1
                prevEnd = end
        return res