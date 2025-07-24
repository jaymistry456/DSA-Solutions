# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # TC: O(4^n), SC: O(n)
        if not digits:
            return []
        hashmap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        n = len(digits)
        res = []
        currArr = []
        def backtrack(i):
            if i == n:
                res.append(''.join(currArr))
                return
            for c in hashmap[digits[i]]:
                currArr.append(c)
                backtrack(i + 1)
                currArr.pop()
        backtrack(0)
        return res