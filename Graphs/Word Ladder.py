# https://leetcode.com/problems/word-ladder/description/

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # brute-force
        # try all 1-letter combination for each word
        # TC: O(n^2*m), SC: O(n)  where n = no of words, m = avg length of each word


        # optimal
        # TC: O(n*m^2), SC: O(n*m)
        if endWord not in wordList:
            return 0
        hashmap = defaultdict(list) # key (pattern) -> value (words matching pattern)
        for i in range(len(wordList)):
            word = wordList[i]
            for j in range(len(word)):
                pattern = word[:j] + '*' + word[j+1:]
                hashmap[pattern].append(word)
        q = deque()
        q.append(beginWord)
        visited = set()
        visited.add(beginWord)
        res = 1
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for i in range(len(word)):
                    pattern = word[:i] + '*' + word[i+1:]
                    for nei in hashmap[pattern]:
                        if nei not in visited:
                            q.append(nei)
                            visited.add(nei)
            res += 1
        return 0