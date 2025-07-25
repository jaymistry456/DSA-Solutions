# https://leetcode.com/problems/gas-station/

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # brute-force
        # TC: O(n^2), SC: O(1)
        n = len(gas)
        if sum(gas) < sum(cost):
            return -1
        for i in range(n):
            tank = gas[i] - cost[i]
            if tank < 0:
                continue
            j = (i + 1) % n
            while j != i:
                tank += gas[j]
                tank -= cost[j]
                if tank < 0:
                    break
                j += 1
                j %= n
            if j == i:
                return i
        return -1


        # optimal
        # TC: O(n), SC: O(1)
        n = len(gas)
        if sum(gas) < sum(cost):
            return -1
        res = 0
        tank = 0
        for i in range(n):
            tank += gas[i]
            tank -= cost[i]
            if tank < 0:
                res = i + 1
                tank = 0
        return res