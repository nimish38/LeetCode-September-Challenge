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
        curr = self.dick
        for i in range(len(word)):
            char = word[i]
            if char == '.':
                print('fuck')
            elif char not in curr:
                return False
            else:
                curr = curr[char]
        if curr['*']:
            return True
        return False
    