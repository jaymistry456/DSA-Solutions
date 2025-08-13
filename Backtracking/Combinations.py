# https://leetcode.com/problems/combinations/description/

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # TC: O((n k)*k), O((n k)*k)
        currRes = []
        res = []
        def dfs(i, currK):
            if currK == 0:
                res.append(currRes.copy())
                return
            if i > n:
                return
            # skip
            dfs(i + 1, currK)
            # include
            currRes.append(i)
            dfs(i + 1, currK - 1)
            currRes.pop()
        dfs(1, k)
        return res