# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # two-pass
        # TC: O(n), SC: O(1)
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        for _ in range(length - n):
            prev = prev.next
        prev.next = prev.next.next
        return dummy.next


        # optimal (one-pass)
        # TC: O(n), SC: O(1)
        dummy = ListNode()
        dummy.next = head
        l = dummy
        r = head
        for _ in range(n):
            r = r.next
        while r:
            l = l.next
            r = r.next
        l.next = l.next.next
        return dummy.next