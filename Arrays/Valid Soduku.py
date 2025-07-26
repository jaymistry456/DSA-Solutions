# https://leetcode.com/problems/valid-sudoku/

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # TC: O(1), SC: O(1)
        # grids
        m = len(board)
        n = len(board[0])
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                hashset = set()
                for i in range(r, r + 3):
                    for j in range(c, c + 3):
                        if board[i][j] != '.':
                            if board[i][j] in hashset:
                                return False
                            hashset.add(board[i][j])
        # rows
        for r in range(m):
            hashset = set()
            for c in range(n):
                if board[r][c] != '.':
                    if board[r][c] in hashset:
                        return False
                    hashset.add(board[r][c])
        # columns
        for c in range(n):
            hashset = set()
            for r in range(m):
                if board[r][c] != '.':
                    if board[r][c] in hashset:
                        return False
                    hashset.add(board[r][c])
        return True