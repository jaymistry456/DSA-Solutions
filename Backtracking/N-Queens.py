# https://leetcode.com/problems/n-queens/description/

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # brute-force
        # TC: O(n!), SC: O(n^2)
        currRes = [["."] * n for _ in range(n)]
        res = []
        def isValid(r, c):
            for i in range(n):
                if currRes[i][c] == "Q" or currRes[r][i] == "Q":
                    return False
            i = r
            j = c
            while i >= 0 and j >= 0:
                if currRes[i][j] == "Q":
                    return False
                i -= 1
                j -= 1
            i = r
            j = c
            while i >= 0 and j < n:
                if currRes[i][j] == "Q":
                    return False
                i -= 1
                j += 1
            return True
        def backtrack(i):
            if i == n:
                res.append(["".join(r) for r in currRes])
                return
            for j in range(n):
                if isValid(i, j):
                    currRes[i][j] = "Q"
                    backtrack(i + 1)
                    currRes[i][j] = "."
        backtrack(0)
        return res


        # optimal
        # TC: O(n!), SC: O(n^2)
        colSet = set()
        posDiagSet = set()
        negDiagSet = set()
        currRes = [["."] * n for _ in range(n)]
        res = []
        def backtrack(i):
            if i == n:
                res.append(["".join(row) for row in currRes])
                return
            for j in range(n):
                if j not in colSet and i + j not in posDiagSet and i - j not in negDiagSet:
                    colSet.add(j)
                    posDiagSet.add(i + j)
                    negDiagSet.add(i - j)
                    currRes[i][j] = "Q"
                    backtrack(i + 1)
                    colSet.remove(j)
                    posDiagSet.remove(i + j)
                    negDiagSet.remove(i - j)
                    currRes[i][j] = "."
        backtrack(0)
        return res