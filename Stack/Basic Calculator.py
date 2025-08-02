# https://leetcode.com/problems/basic-calculator/

class Solution:
    def calculate(self, s: str) -> int:
        # TC: O(n), SC: O(n)
        res = 0
        curr = 0
        sign = 1
        stack = []
        for i in range(len(s)):
            char = s[i]
            if char.isdigit():
                curr = curr * 10 + int(char)
            elif char == '+':
                res += sign * curr
                sign = 1
                curr = 0
            elif char == '-':
                res += sign * curr
                sign = -1
                curr = 0
            elif char == '(':
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif char == ')':
                res += sign * curr
                res *= stack.pop()
                res += stack.pop()
                curr = 0
        res += sign * curr
        return res