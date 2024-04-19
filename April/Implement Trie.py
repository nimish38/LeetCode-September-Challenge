class Trie:
    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        curr = self.trie
        for letter in word:
            if curr[letter]  not in curr:
                curr[letter] = {}
            curr = curr[letter]
        curr[letter] = '*'

    def search(self, word: str) -> bool:
        curr = self.trie
        for letter in word:
            if letter not in curr:
                return False
            curr = curr[letter]
        if curr[letter] == '*':
            return True

    def startsWith(self, prefix: str) -> bool:
        curr = self.trie
        for letter in prefix:
            if letter not in curr:
                return False
        return True

