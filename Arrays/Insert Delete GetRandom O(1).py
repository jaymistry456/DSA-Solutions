# https://leetcode.com/problems/insert-delete-getrandom-o1/

# TC: O(1) for each function
class RandomizedSet:

    def __init__(self):
        self.hashmap = {}   # key (val) -> value (index of val in arr)
        self.arr = []

    def insert(self, val: int) -> bool:
        res = val not in self.hashmap
        if res:
            self.hashmap[val] = len(self.arr)
            self.arr.append(val)
        return res

    def remove(self, val: int) -> bool:
        res = val in self.hashmap
        if res:
            lastVal = self.arr[-1]
            valIndex = self.hashmap[val]
            self.hashmap[lastVal] = valIndex
            self.arr[valIndex] = lastVal
            del self.hashmap[val]
            self.arr.pop()
        return res

    def getRandom(self) -> int:
        return random.choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()