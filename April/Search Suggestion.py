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

    def getwords(self, prefix, let, curr):
        stack, res = [(let, curr[let])], []
        while stack and len(res) < 3:
            item = stack.pop()
            for char in sorted(item[1], reverse=True):
                if char == '*':
                    res.append(prefix + item[0])
                else:
                    stack.append((item[0] + char, item[1][char]))
        if len(res) > 3:
            return res[:3]
        return res

    def suggestions(self, searchWord):
        res, prefix = [], ''
        curr = self.trie
        for letter in searchWord:
            if letter in curr:
                res.append(self.getwords(prefix, letter, curr))
                curr = curr[letter]
                prefix += letter
            else:
                break
        while len(res) < len(searchWord):
            res.append([])
        return res

class Solution:
    def suggestedProducts(self, products, searchWord):
        trie = Trie()
        for word in products:
            trie.insert(word)
        return trie.suggestions(searchWord)

print(Solution().suggestedProducts(products = ["havana"], searchWord = "havana"))