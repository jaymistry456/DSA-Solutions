# https://leetcode.com/problems/decode-string/description/

class Solution:
    def decodeString(self, s: str) -> str:
        # TC: O(n), SC: O(n)
        stack = []
        res = ""
        currNum = 0
        for i in range(len(s)):
            char = s[i]
            if char == "[":
                stack.append(res)
                stack.append(currNum)
                res = ""
                currNum = 0
            elif char == "]":
                prevNum = stack.pop()
                prevStr = stack.pop()
                res = prevStr + prevNum * res
            elif ord("0") <= ord(char) <= ord("9"):
                currNum = currNum * 10 + int(char)
            else:
                res += char
        return res