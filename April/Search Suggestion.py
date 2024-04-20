class Trie:
    def __init__(self):
        self.trie = {}

    def insert(self, word):
        curr = self.trie
        for letter in word:
            if letter not in curr:
                curr[letter] = {}
            curr = curr[letter]
        curr['*'] = True

class Solution:
    def suggestedProducts(self, products, searchWord):
        trie = Trie()
        for word in products:
            trie.insert(word)
        return trie.suggestions(searchWord)
