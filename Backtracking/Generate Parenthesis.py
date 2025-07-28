# https://leetcode.com/problems/generate-parentheses/description/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # brute-force
        # TC: O(n * 2^2n), SC: O(n*2^2n)
        def isValid(s):
            curr = 0
            for i in range(len(s)):
                if s[i] == '(':
                    curr += 1
                else:
                    curr -= 1
                if curr < 0:
                    return False
            return curr == 0
        res = []
        def backtrack(s):
            if len(s) == n * 2:
                if isValid(s):
                    res.append(s)
                return
            backtrack(s + '(')
            backtrack(s + ')')
        backtrack('')
        return res


        # optimal
        # TC: O(n * 2^2n), SC: O(n)
        res = []
        def backtrack(s, open, closed):
            if len(s) == 2 * n:
                res.append(s)
                return
            if open < n:
                backtrack(s + '(', open + 1, closed)
            if closed < open:
                backtrack(s + ')', open, closed + 1)
        backtrack('', 0, 0)
        return res