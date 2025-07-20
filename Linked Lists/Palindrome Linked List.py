# https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # brute-force
        # TC: O(n), SC: O(n)
        arr = []
        node = head
        while node:
            arr.append(node.val)
            node = node.next
        l = 0
        r = len(arr) - 1
        while l < r:
            if arr[l] != arr[r]:
                return False
            l += 1
            r -= 1
        return True


        # optimal
        # TC: O(n), SC: O(1)
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        l = head
        r = prev
        while r:
            if l.val != r.val:
                return False
            l = l.next
            r = r.next
        return True