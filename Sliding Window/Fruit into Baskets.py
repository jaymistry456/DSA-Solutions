# https://leetcode.com/problems/fruit-into-baskets/

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # brute-force
        # TC: O(n^2), SC: O(1)
        res = 0
        n = len(fruits)
        for i in range(n):
            j = i
            hashset = set()
            while j < n:
                if fruits[j] not in hashset and len(hashset) == 2:
                    break
                res = max(res, j - i + 1)
                hashset.add(fruits[j])
                j += 1
        return res


        # optimal
        # TC: O(n), SC: O(1)
        l = 0
        r = 0
        n = len(fruits)
        hashmap = {}    # fruit -> freq of fruit
        res = 0
        while r < n:
            if fruits[r] in hashmap:
                hashmap[fruits[r]] += 1
            else:
                hashmap[fruits[r]] = 1
            while len(hashmap) > 2:
                hashmap[fruits[l]] -= 1
                if hashmap[fruits[l]] == 0:
                    del hashmap[fruits[l]]
                l += 1
            res = max(res, r - l + 1)
            r += 1
        return res