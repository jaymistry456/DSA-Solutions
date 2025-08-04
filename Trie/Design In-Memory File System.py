# https://leetcode.ca/all/588.html

class TrieNode:
    def __init__(self):
        self.children = {}  # key (directory name) -> value (TrieNode)
        self.content = []   # list of file in this directory
        self.isFile = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, path, isFile):
        curr = self.root
        if path == "/":
            return curr
        parts = path.split("/")[1:]    # skip the empty directory at the start
        for part in parts:
            if part not in curr.children:
                curr.children[part] = TrieNode()
            curr = curr.children[part]
        curr.isFile = isFile

    def search(self, path):
        curr = self.root
        if path == "/":
            return curr
        parts = path.split("/")[1:]    # skip the empty directory at the start
        for part in parts:
            if part not in curr.children:
                return None
            curr = curr.children[part]
        return curr
    
class FileSystem:
    def __init__(self):
        self.trie = Trie()
        
    def ls(self, path):
        node = self.trie.search(path)
        if not node:
            return []
        if node.isFile:
            return [path.split("/")[-1]]
        return sorted(node.children.keys())
    
    def mkdir(self, path):
        self.trie.insert(path, False)

    def addContentToFile(self, filePath, content):
        node = self.trie.search(filePath)
        if node:
            node.isFile = True
            node.content.append(content)
        else:
            self.trie.insert(filePath, True)
            node = self.trie.search(filePath)
            node.content.append(content)

    def readContentFromFile(self, filePath):
        node = self.trie.search(filePath)
        if node:
            return ''.join(node.content)
        return ''