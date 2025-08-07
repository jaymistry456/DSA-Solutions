# https://leetcode.com/problems/reorganize-string/

class Solution:
    def reorganizeString(self, s: str) -> str:
        # brute-force
        # TC: O(n*n!), SC: O(n!)
        # generate all permutation of the strings
        # check the validity of each permutation

        
        # optimal
        # TC: O(n), SC: O(1)
        hashmap = {}    # char -> freq of char
        for i in range(len(s)):
            if s[i] in hashmap:
                hashmap[s[i]] += 1
            else:
                hashmap[s[i]] = 1
        maxHeap = [(-freq, char) for char, freq in hashmap.items()]
        heapq.heapify(maxHeap)
        q = deque()    # (-freq, char, turn)
        currTurn = 0
        res = ''
        while maxHeap or q:
            while q and q[0][2] <= currTurn:
                freq, char, turn = q.popleft()
                heapq.heappush(maxHeap, (freq, char))
            if maxHeap:
                freq, char = heapq.heappop(maxHeap)
                res += char
                freq += 1
                if freq != 0:
                    q.append((freq, char, currTurn + 2))
            else:
                return ""
            currTurn += 1
        return res