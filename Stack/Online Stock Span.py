# https://leetcode.com/problems/online-stock-span/description/

# brute-force
# TC: O(n^2), SC: O(n)
class StockSpanner:

    def __init__(self):
        self.stock = []

    def next(self, price: int) -> int:
        self.stock.append(price)
        curr = 1
        for i in range(len(self.stock) - 2, -1, -1):
            if self.stock[i] <= self.stock[-1]:
                curr += 1
            else:
                break
        return curr


# optimal
# TC: O(n), SC: O(n)
class StockSpanner:

    def __init__(self):
        self.stack = []    # (stock, span)

    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        self.stack.append((price, span))
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)