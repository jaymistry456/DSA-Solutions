# https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # TC: O(m+n), SC: O(1)
        a = a[::-1]
        b = b[::-1]
        carry = 0
        res = ''
        for i in range(max(len(a), len(b))):
            digitA = ord(a[i]) - ord('0') if i < len(a) else 0
            digitB = ord(b[i]) - ord('0') if i < len(b) else 0
            total = digitA + digitB + carry
            carry = total // 2
            total = total % 2
            res += str(total)
        if carry == 1:
            res += '1'
        return res[::-1]