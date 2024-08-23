class Trie:

    def __init__(self):
        self.trie = set()

    def insert(self, word: str) -> None:
        curr = self.trie
        for char in word:
            if char not in curr:
                curr[char] = set()
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

    def startsWith(self, prefix: str) -> bool: