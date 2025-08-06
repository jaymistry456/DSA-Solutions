# https://leetcode.com/problems/sudoku-solver/

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # brute-force
        # TC: O(9^empty), SC: O(empty)
        m = len(board)
        n = len(board[0])
        def isValid(r, c, char):
            # rows and columns
            for i in range(9):
                if board[i][c] == char or board[r][i] == char:
                    return False
            # 3x3 grids
            rows = (r // 3) * 3
            cols = (c // 3) * 3
            for i in range(rows, rows + 3):
                for j in range(cols, cols + 3):
                    if board[i][j] == char:
                        return False
            return True
        def backtrack():
            for r in range(m):
                for c in range(n):
                    if board[r][c] == ".":
                        for char in "123456789":
                            if isValid(r, c, char):
                                board[r][c] = char
                                if backtrack():
                                    return True
                                board[r][c] = "."
                        return False
            return True
        backtrack()


        # optimal
        # TC: O(9^empty), SC: O(empty)
        m = len(board)
        n = len(board[0])
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty = []
        for r in range(m):
            for c in range(n):
                if board[r][c] == ".":
                    empty.append((r, c))
                else:
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    box = (r // 3) * 3 + c // 3
                    boxes[box].add(board[r][c])
        def backtrack(i):
            if i == len(empty):
                return True
            r, c = empty[i]
            box = (r // 3) * 3 + c // 3
            for char in "123456789":
                if char not in rows[r] and char not in cols[c] and char not in boxes[box]:
                    board[r][c] = char
                    rows[r].add(char)
                    cols[c].add(char)
                    boxes[box].add(char)
                    if backtrack(i + 1):
                        return True
                    board[r][c] = "."
                    rows[r].remove(char)
                    cols[c].remove(char)
                    boxes[box].remove(char)
        backtrack(0)