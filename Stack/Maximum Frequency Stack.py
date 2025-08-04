# https://leetcode.com/problems/maximum-frequency-stack/

# TC: O(1), SC: O(n)
class FreqStack:

    def __init__(self):
        self.hashmap = defaultdict(int) # key (num) -> value (freq of num)
        self.group = defaultdict(list)  # key (freq) -> value (list of nums with this freq)
        self.currMaxFreq = 0

    def push(self, val: int) -> None:
        self.hashmap[val] += 1
        self.group[self.hashmap[val]].append(val)
        self.currMaxFreq = max(self.currMaxFreq, self.hashmap[val])

    def pop(self) -> int:
        currTop = self.group[self.currMaxFreq].pop()
        self.hashmap[currTop] -= 1
        if not self.group[self.currMaxFreq]:
            self.currMaxFreq -= 1
        return currTop


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()