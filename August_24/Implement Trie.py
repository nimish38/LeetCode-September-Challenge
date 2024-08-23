class Trie:
    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        curr = self.trie
        for char in word:
            if char not in curr:
                curr[char] = {}
            curr = curr[char]
        curr['*'] = True

    def search(self, word: str) -> bool:
        curr = self.trie
        for char in word:
            if char not in curr:
                return False
            curr = curr[char]
        if '*' in curr:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        curr = self.trie
        for char in prefix:
            if char not in curr:
                return False
            curr = curr[char]
        return True

trie =Trie()
trie.insert("apple")
print(trie.search("apple"))
print(trie.search("app"))
print(trie.startsWith("app"))
trie.insert("app")
print(trie.search("app"))
print(trie.search('bhosad'))