# https://leetcode.com/problems/copy-list-with-random-pointer/description/

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # TC: O(n), SC: O(n)
        hashmap = {}    # original node -> new node
        curr = head
        while curr:
            hashmap[curr] = Node(curr.val)
            curr = curr.next
        for node1, node2 in hashmap.items():
            if node1.next:
                node2.next = hashmap[node1.next]
            if node1.random:
                node2.random = hashmap[node1.random]
        return hashmap[head] if head else None