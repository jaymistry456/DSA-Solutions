# https://leetcode.com/problems/spiral-matrix/

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        t = 0
        b = len(matrix) - 1
        l = 0
        r = len(matrix[0]) - 1
        while l <= r and t <= b:
            # left to right
            for k in range(l, r + 1):
                res.append(matrix[t][k])
            t += 1
            # top to bottom
            for k in range(t, b + 1):
                res.append(matrix[k][r])
            r -= 1
            if l > r or t > b:
                break
            # right to left
            for k in range(r, l - 1, -1):
                res.append(matrix[b][k])
            b -= 1
            # bottom to top
            for k in range(b, t - 1, -1):
                res.append(matrix[k][l])
            l += 1
        return res