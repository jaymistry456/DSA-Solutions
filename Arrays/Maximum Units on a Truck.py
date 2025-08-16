# https://leetcode.com/problems/maximum-units-on-a-truck/description/

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # TC: O(nlogn), SC: O(1)
        boxTypes.sort(key=lambda x:x[1], reverse=True)    # sort boxes by no. of units in them
        res = 0
        for i in range(len(boxTypes)):
            if truckSize == 0:
                break
            currBoxes, currUnits = boxTypes[i]
            boxes = min(truckSize, currBoxes)
            res += boxes * currUnits
            truckSize -= boxes
        return res