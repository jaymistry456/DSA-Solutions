# https://leetcode.com/problems/palindrome-number/description/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # TC: O(logn), SC: O(1)
        if x < 0:
            return False
        reverse = 0
        temp = x
        while temp > 0:
            remainder = temp % 10
            reverse = reverse * 10 + remainder
            temp //= 10
        return reverse == x