# https://leetcode.com/problems/longest-common-prefix/description/

# using Trie
# TC: O(m*n), SC: O(m*n)
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def get_root(self):
        return self.root
    
    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.word = True

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie = Trie()
        for s in strs:
            trie.insert(s)

        res = ''
        node = trie.get_root()
        while len(node.children) == 1 and node.word == False:
            char, child = list(node.children.items())[0]
            res += char
            node = child
        return res

        # using simple scanning
        # TC: O(m*n), SC: O(1)
        res = ''
        for i in range(len(strs[0])):
            for s in strs[1:]:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res