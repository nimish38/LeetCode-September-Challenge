class Trie:
    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        curr = self.trie
        for letter in word:
            if letter not in curr:
                curr[letter] = {}
            curr = curr[letter]
        curr['*'] = '*'

    def search(self, word: str) -> bool:
        curr = self.trie
        for letter in word:
            if letter not in curr:
                return False
            curr = curr[letter]
        if '*' in curr:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        curr = self.trie
        for letter in prefix:
            if letter not in curr:
                return False
            curr = curr[letter]
        return True

a = Trie()
print(a.insert('apple'))
print(a.search('apple'))
print(a.search('app'))
print(a.startsWith('app'))
print(a.insert('app'))
print(a.search('app'))
