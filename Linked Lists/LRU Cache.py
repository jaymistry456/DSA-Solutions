# https://leetcode.com/problems/lru-cache/description/

class Node:
    def __init__(self, key=0, value=0, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

class LRUCache:

    # SC: O(capacity)
    def __init__(self, capacity: int):
        self.cache = {} # key (key) -> value (Node with key and value)
        self.capacity = capacity
        self.left = Node()
        self.right = Node()
        self.left.next = self.right
        self.right.prev = self.left

    # TC: O(1), SC: O(1)
    def insertOnRight(self, newNode):
        originalRight = self.right.prev
        newNode.prev = originalRight
        newNode.next = self.right
        originalRight.next = self.right.prev = newNode

    # TC: O(1), SC: O(1)
    def remove(self, node):
        previousNode = node.prev
        nextNode = node.next
        previousNode.next = nextNode
        nextNode.prev = previousNode

    # TC: O(1), SC: O(1)
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insertOnRight(self.cache[key])
            return self.cache[key].value
        return -1

    # TC: O(1), SC: O(1)
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
            self.cache[key].value = value
            self.insertOnRight(self.cache[key])
        else:
            newNode = Node(key, value)
            self.cache[key] = newNode
            self.insertOnRight(newNode)
            if len(self.cache) > self.capacity:
                nodeToRemove = self.left.next
                self.remove(nodeToRemove)
                del self.cache[nodeToRemove.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)