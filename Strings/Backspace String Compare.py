# https://leetcode.com/problems/backspace-string-compare/description/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # TC: O(m+n), SC: O(1)
        def get_next_valid_char(text, k):
            skip = 0
            while k >= 0:
                if text[k] != '#':
                    if skip > 0:
                        skip -= 1
                    else:
                        break
                else:
                    skip += 1
                k -= 1
            return k

        i = len(s) - 1
        j = len(t) - 1
        while i >= 0 or j >= 0:
            i = get_next_valid_char(s, i)
            j = get_next_valid_char(t, j)
            if i >= 0 and j >= 0:
                if s[i] != t[j]:
                    return False
            elif i >= 0 or j >= 0:
                return False
            i -= 1
            j -= 1
        return True