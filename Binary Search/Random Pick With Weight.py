# https://leetcode.com/problems/random-pick-with-weight/

class Solution:

    # brute-force
    # TC: O(sum(w)), SC: O(sum(w))
    def __init__(self, w: List[int]):
        n = len(w)
        self.arr = []
        for i in range(n):
            for j in range(w[i]):
                self.arr.append(i)

    # TC: O(1), SC: O(1)
    def pickIndex(self) -> int:
        return random.choice(self.arr)


class Solution:

    # optimal
    # TC: O(w), SC: O(w)
    def __init__(self, w: List[int]):
        n = len(w)
        self.arr = []
        currSum = 0
        for i in range(n):
            currSum += w[i]
            self.arr.append(currSum)

    # TC: O(logn), SC: O(1)
    def pickIndex(self) -> int:
        target = random.randint(1, self.arr[-1])
        l = 0
        r = len(self.arr) - 1
        while l < r:
            mid = l + (r - l) // 2
            if self.arr[mid] < target:
                l = mid + 1
            else:
                r = mid
        return l


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()


# # Your Solution object will be instantiated and called as such:
# # obj = Solution(w)
# # param_1 = obj.pickIndex()