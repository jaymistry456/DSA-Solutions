# brute-force
class HitCounter:

    # SC: O(n)
    def __init__(self):
        self.hits = []

    # TC: O(1), SC: O(1)
    def hit(self, timestamp: int) -> None:
        self.hits.append(timestamp)

    # TC: O(n), SC: O(n)
    def getHits(self, timestamp: int) -> int:
        res = 0
        for i in range(len(self.hits)):
            if timestamp - 299 <= self.hits[i] <= timestamp:
                res += 1
        return res
    

# better
class HitCounter:

    # SC: O(n)
    def __init__(self):
        self.hits = deque()

    # TC: O(1), SC: O(1)
    def hit(self, timestamp: int) -> None:
        self.hits.append(timestamp)

    # TC: O(k), SC: O(1)    k = no. of outdated operations
    def getHits(self, timestamp: int) -> int:
        while self.hits and self.hits[0] <= timestamp - 300:
            self.hits.popleft()
        return len(self.hits)
    

# optimal
class HitCounter:

    # SC: O(n)
    def __init__(self):
        self.hits = []

    # TC: O(1), SC: O(1)
    def hit(self, timestamp: int) -> None:
        self.hits.append(timestamp)

    # TC: O(logn), SC: O(1)
    def getHits(self, timestamp: int) -> int:
        l = 0
        r = len(self.hits)
        target = timestamp - 300
        while l < r:
            mid = l + (r - l) // 2
            if self.hits[mid] <= target:
                l = mid + 1
            else:
                r = mid
        return len(self.hits) - l