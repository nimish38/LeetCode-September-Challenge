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
        return self.regexSearch(word, self.dick)

    def regexSearch(self, word, curr):
        for i in range(len(word)):
            char = word[i]
            if char == '.':
                for item in curr:
                    if self.regexSearch(word[i + 1:], curr[item]):
                        return True
                return False
            elif char not in curr:
                return False
            else:
                curr = curr[char]
        if curr['*']:
            return True
        return False

wordDictionary = WordDictionary()
wordDictionary.addWord("bad")
wordDictionary.addWord("dad")
wordDictionary.addWord("mad")
print(wordDictionary.search("pad"))
print(wordDictionary.search("bad"))
print(wordDictionary.search(".ad"))
print(wordDictionary.search("b.."))