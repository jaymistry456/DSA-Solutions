# https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # brute-force
        # TC: O(m*n), SC: O(1)
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == target:
                    return True
        return False


        # optimal
        # TC: O(logm+logn), SC: O(1)
        m = len(matrix)
        n = len(matrix[0])
        l = 0
        r = m * n - 1
        while l <= r:
            mid = l + (r - l) // 2
            i = mid // n
            j = mid % n
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False