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
        if not isinstance(curr, dict):
            return False
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
        if '*' in curr:
            return True
        return False

wordDictionary = WordDictionary()
wordDictionary.addWord("a")
print(wordDictionary.search("."))
print(wordDictionary.search(".a"))
print(wordDictionary.search("a."))
# print(wordDictionary.search("b.."))