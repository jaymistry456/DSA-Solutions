# https://leetcode.com/problems/longest-valid-parentheses/description/

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # brute-force
        # TC: O(n^2), SC: O(n)
        n = len(s)
        res = 0
        for i in range(n):
            stack = []
            for j in range(i, n):
                if s[j] == ')':
                    if not stack or stack[-1] != '(':
                        break
                    stack.pop()
                else:
                    stack.append(s[i])
                if len(stack) == 0:
                    res = max(res, j - i + 1)
        return res


        # optimal
        # TC: O(n), SC: O(n)
        stack = [-1]
        res = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    res = max(res, i - stack[-1])
        return res