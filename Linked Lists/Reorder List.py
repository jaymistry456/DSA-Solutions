# https://leetcode.com/problems/reorder-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # TC: O(n), SC: O(1)
        # split the linked list
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        left = head
        right = slow.next
        slow.next = None
        # reverse the second half
        prev = None
        curr = right
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        # merge the lists together
        l1 = head
        l2 = prev
        while l1 and l2:
            first = l1.next
            second = l2.next
            l1.next = l2
            l2.next = first
            l1 = first
            l2 = second