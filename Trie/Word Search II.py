# https://leetcode.com/problems/word-search-ii/

class TrieNode:
    def __init__(self):
        self.children = {}    # char -> TrieNode()
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # brute-force
        # TC: O(m*n*w*4^l), SC: O(l)
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        m = len(board)
        n = len(board[0])
        def dfs(r, c, word, i, visited):
            if board[r][c] != word[i]:
                return False
            if i == len(word) - 1:
                return True
            visited.add((r, c))
            for dr, dc in directions:
                if 0 <= r + dr < m and 0 <= c + dc < n and (r + dr, c + dc) not in visited:
                    if dfs(r + dr, c + dc, word, i + 1, visited):
                        return True
            visited.remove((r, c))
            return False
        res = set()
        for word in words:
            for r in range(m):
                for c in range(n):
                    if dfs(r, c, word, 0, set()):
                        res.add(word)
        return list(res)


        # optimal
        # TC: O(m*n*w*4^l), SC: O(w*l)
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        m = len(board)
        n = len(board[0])
        trie = Trie()
        for word in words:
            trie.insert(word)
        res = set()
        def dfs(r, c, currNode, path, visited):
            char = board[r][c]
            if char not in currNode.children:
                return
            visited.add((r, c))
            currNode = currNode.children[char]
            path += char
            if currNode.isWord:
                res.add(path)
            for dr, dc in directions:
                if 0 <= r + dr < m and 0 <= c + dc < n and (r + dr, c + dc) not in visited:
                    dfs(r + dr, c + dc, currNode, path, visited)
            visited.remove((r, c))
        for r in range(m):
            for c in range(n):
                dfs(r, c, trie.root, '', set())
        return list(res)