# https://leetcode.com/problems/rotate-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # TC: O(n), SC: O(1)
        if not head:
            return head
        # calculate length of linked list
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        # go to the point of splitting
        l = head
        r = head
        for _ in range(k % length):
            r = r.next
        while r.next:
            l = l.next
            r = r.next
        # bring the second half to the front
        if l.next:
            newHead = head
            newHead = l.next
            l.next = None
            r.next = head
            return newHead
        else:
            return head