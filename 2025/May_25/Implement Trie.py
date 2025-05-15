class Trie(object):

    def __init__(self):
        self.trie = {}

    def insert(self, word):
        curr = self.trie
        for c in word:
            if c not in curr:
                curr[c] ={}
            curr = curr[c]
        curr['*'] = True

    def search(self, word):
        curr = self.trie
        for c in word:
            if c not in curr:
                return False
            curr = curr[c]
        return True if '*' in curr else False

    def startsWith(self, prefix):
        curr = self.trie
        for c in prefix:
            if c not in curr:
                return False
            curr = curr[c]
        return True
