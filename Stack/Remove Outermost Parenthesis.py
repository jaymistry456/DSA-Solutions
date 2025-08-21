# https://leetcode.com/problems/remove-outermost-parentheses/

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        # brute-force
        # TC: O(n), SC: O(n)
        stack = []
        res = ""
        for char in s:
            if char == "(":
                if stack:
                    res += char
                stack.append(char)
            else:
                stack.pop()
                if stack:
                    res += char
        return res
        
        # optimal
        # TC: O(n), SC: O(1)
        curr = 0
        res = ""
        for char in s:
            if char == "(":
                if curr > 0:
                    res += char
                curr += 1
            else:
                curr -= 1
                if curr > 0:
                    res += char
        return res