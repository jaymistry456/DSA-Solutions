# https://leetcode.com/problems/time-based-key-value-store/description/

class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)   # key (key) -> value (array of (timestamp, value) pairs)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        # brute-force
        # TC: O(values), SC: O(values)
        values = self.map[key]
        n = len(values)
        for i in range(n - 1, -1, -1):
            currTimestamp, currValue = values[i]
            if currTimestamp <= timestamp:
                return currValue
        return ''

        # optimal
        # TC: O(logvalues), SC: O(values)
        values = self.map[key]
        n = len(values)
        # binary search
        res = ''
        l = 0
        r = n - 1
        while l <= r:
            mid = l + (r - l) // 2
            currTimestamp, currValue = values[mid]
            if currTimestamp <= timestamp:
                res = currValue
                l = mid + 1
            else:
                r = mid - 1
        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)