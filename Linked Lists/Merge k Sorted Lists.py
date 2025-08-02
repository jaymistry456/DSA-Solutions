# https://leetcode.com/problems/merge-k-sorted-lists/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # brute-force
        # TC: O(nlogn), SC: O(n)
        values = []
        for head in lists:
            while head:
                values.append(head.val)
                head = head.next
        values.sort()
        dummy = newHead = ListNode()
        for i in range(len(values)):
            dummy.next = ListNode(values[i])
            dummy = dummy.next
        return newHead.next


        # optimal
        # TC: O(logk), SC: O(1)
        if not lists:
            return None
        def mergeTwoLists(l1, l2):
            dummy = curr = ListNode()
            while l1 and l2:
                if l1.val <= l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next
            if l1:
                curr.next = l1
            if l2:
                curr.next = l2
            return dummy.next
        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                mergedLists.append(mergeTwoLists(l1, l2))
            lists = mergedLists
        return lists[-1]