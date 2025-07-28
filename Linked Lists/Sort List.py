# https://leetcode.com/problems/sort-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # brute-force
        # TC: O(nlogn), SC: O(n)
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        arr.sort()
        curr = head
        for i in range(len(arr)):
            curr.val = arr[i]
            curr = curr.next
        return head


        # optimal
        # TC: O(nlogn), SC: O(logn)
        def getMid(curr):
            slow = curr
            fast = curr.next
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            return slow
        def merge(l1, l2):
            dummy = ListNode()
            curr = dummy
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
        def mergeSort(head):
            if not head or not head.next:
                return head
            mid = getMid(head)
            l1 = head
            l2 = mid.next
            mid.next = None
            l1Sorted = mergeSort(l1)
            l2Sorted = mergeSort(l2)
            return merge(l1Sorted, l2Sorted)
        return mergeSort(head)