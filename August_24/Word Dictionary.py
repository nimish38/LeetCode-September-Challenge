class WordDictionary:
    def __init__(self):
        self.dick = {}

    def addWord(self, word: str) -> None:
        curr = self.dick
        for char in word:
            if char not in curr:
                curr[char] = {}
            curr = curr[char]
        curr['*'] = True

    def search(self, word: str) -> bool: