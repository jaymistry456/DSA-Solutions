# https://leetcode.com/problems/reverse-nodes-in-k-group/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # TC: O(n), SC: O(n/k)
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next
        if length < k:
            return head
        prev = None
        curr = head
        for _ in range(k):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        head.next = self.reverseKGroup(curr, k)
        return prev