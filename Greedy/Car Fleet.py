# https://leetcode.com/problems/car-fleet/

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # TC: O(nlogn), SC: O(n)
        arr = sorted(zip(position, speed), reverse=True)
        res = 0
        currMaxTime = 0
        for p, s in arr:
            currTime = (target - p) / s
            if currTime > currMaxTime:
                res += 1
                currMaxTime = currTime
        return res