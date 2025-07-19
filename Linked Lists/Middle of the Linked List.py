# https://leetcode.com/problems/middle-of-the-linked-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # brute-force
        # TC: O(n), SC: O(1)
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        curr = head
        for i in range(length // 2):
            curr = curr.next
        return curr


        # optimal
        # TC: O(n), SC: O(1)
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow