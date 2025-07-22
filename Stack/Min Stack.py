# https://leetcode.com/problems/min-stack/description/

class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    # TC: O(1)
    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(val)
            self.minStack.append(val)
        else:
            self.stack.append(val)
            self.minStack.append(min(self.minStack[-1], val))

    # TC: O(1)
    def pop(self) -> None:
        self.minStack.pop()
        return self.stack.pop()

    # TC: O(1)
    def top(self) -> int:
        return self.stack[-1]

    # TC: O(1)
    def getMin(self) -> int:
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()