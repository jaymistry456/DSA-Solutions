# https://leetcode.com/problems/minimum-window-substring/description/

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # brute-force
        # TC: O(m^3), SC: O(1)
        m = len(s)
        n = len(t)
        if m < n:
            return ''
        res = ''
        minLength = float('inf')
        for i in range(m):
            for j in range(i, m):
                flag = True
                substring = s[i:j+1]
                hashmap = {}    # key (char) -> value (freq of char)
                for char in substring:
                    if char in hashmap:
                        hashmap[char] += 1
                    else:
                        hashmap[char] = 1
                for char in t:
                    if char in hashmap:
                        hashmap[char] -= 1
                        if hashmap[char] == 0:
                            del hashmap[char]
                    else:
                        flag = False
                        break
                if flag and j - i + 1 < minLength:
                    minLength = j - i + 1
                    res = substring        
        return res


        # optimal
        # TC: O(m+n), SC: O(1)
        m = len(s)
        n = len(t)
        if m < n:
            return ''
        need = 0
        hashmapT = defaultdict(int)   # key (char) -> value (freq of char)
        for i in range(n):
            need += 1
            hashmapT[t[i]] += 1
        hashmapS = defaultdict(int)
        l = 0
        r = 0
        haves = 0
        minLength = float('inf')
        res = ''
        while r < m:
            hashmapS[s[r]] += 1
            if hashmapS[s[r]] <= hashmapT[s[r]]:
                haves += 1
            while haves == need and l <= r:
                if r - l + 1 < minLength:
                    minLength = r - l + 1
                    res = s[l:r+1]
                hashmapS[s[l]] -= 1
                if hashmapS[s[l]] < hashmapT[s[l]]:
                    haves -= 1
                    l += 1
                    break
                l += 1
            r += 1
        return res