# https://leetcode.com/problems/basic-calculator-ii/description/

class Solution:
    def calculate(self, s: str) -> int:
        # TC: O(n), SC: O(n)
        stack = []
        n = len(s)
        curr = 0
        sign = '+'
        for i in range(n):
            char = s[i]
            if char.isdigit():
                curr = curr * 10 + int(char)
            if char in '+-*/' or i == n - 1:
                if sign == '+':
                    stack.append(curr)
                elif sign == '-':
                    stack.append(-curr)
                elif sign == '*':
                    stack.append(stack.pop() * curr)
                elif sign == '/':
                    stack.append(int(stack.pop() / curr))
                sign = char
                curr = 0
        return sum(stack)