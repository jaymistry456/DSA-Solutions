# https://leetcode.com/problems/implement-trie-prefix-tree/description/

class TrieNode:
    def __init__(self):
        self.children = {}  # key (character) -> value (TrieNode)
        self.word = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    # TC: O(n), SC: O(n)
    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.word = True

    # TC: O(n), SC: O(1)
    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.word

    # TC: O(n), SC: O(1)
    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)