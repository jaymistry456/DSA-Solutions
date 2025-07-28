# https://leetcode.com/problems/add-two-numbers/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # TC: O(m+n), SC: O(m+n)
        carry = 0
        dummy = ListNode()
        curr = dummy
        while l1 and l2:
            sum = (l1.val + l2.val + carry) % 10
            carry = (l1.val + l2.val + carry) // 10
            curr.next = ListNode(sum)
            l1 = l1.next
            l2 = l2.next
            curr = curr.next
        while l1:
            sum = (l1.val + carry) % 10
            carry = (l1.val + carry) // 10
            curr.next = ListNode(sum)
            l1 = l1.next
            curr = curr.next
        while l2:
            sum = (l2.val + carry) % 10
            carry = (l2.val + carry) // 10
            curr.next = ListNode(sum)
            l2 = l2.next
            curr = curr.next
        if carry:
            curr.next = ListNode(carry)
        return dummy.next