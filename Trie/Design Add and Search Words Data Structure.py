# https://leetcode.com/problems/design-add-and-search-words-data-structure/description/

# brute-force
class WordDictionary:

    def __init__(self):
        self.words = []
        
    # TC: O(1)
    def addWord(self, word: str) -> None:
        self.words.append(word)

    # TC: O(m*n)
    def search(self, word: str) -> bool:
        for w in self.words:
            if len(w) != len(word):
                continue
            i = 0
            while i < len(word):
                if word[i] == w[i] or word[i] == '.':
                    i += 1
                else:
                    break
            if i == len(word):
                return True
        return False


# optimal
class TrieNode:
    
    def __init__(self):
        self.children = {}  # key (char) -> value (TrieNode)
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    # TC: O(m), SC: O(m)
    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isWord = True

    def dfs(self, curr, word):
        for i in range(len(word)):
            if word[i] == '.':
                for child in curr.children:
                    if self.dfs(curr.children[child], word[i+1:]):
                        return True
                return False
            else:
                if word[i] not in curr.children:
                    return False
                curr = curr.children[word[i]]
        return curr.isWord

    # TC: O(m), SC: O(m)
    def search(self, word: str) -> bool:
        return self.dfs(self.root, word)

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)