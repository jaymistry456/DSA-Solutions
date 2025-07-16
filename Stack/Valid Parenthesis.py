# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        # brute force
        # TC: O(n^2), SC: O(n)
        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('()', '')
            s = s.replace('{}', '')
            s = s.replace('[]', '')
        return s == ''

        # optimal
        # TC: O(n), SC: O(n)
        stack = []  # push only open brackets, pops when close brackets
        hashmap = {')': '(', '}': '{', ']': '['}    # key -> close bracket, value -> open bracket
        for b in s:
            if b in '({[':
                stack.append(b)
            else:
                if not stack or stack[-1] != hashmap[b]:
                    return False
                stack.pop()

        return not stack
                    