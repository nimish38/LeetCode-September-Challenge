class WordDictionary(object):

    def __init__(self):
        self.trie = {}

    def addWord(self, word):
        curr = self.trie
        for c in word:
            if c not in curr:
                curr[c] = {}
            curr = curr[c]
        curr['*'] = True

    def search(self, word):
        def  solve(curr, ind):
            if ind == len(word):
                if '*' in curr:
                    return True
                return False
            if word[ind] == '.':
                for char in curr:
                    if solve(curr[char], ind + 1):
                        return True
                return False
            else:
                if word[ind] not in curr:
                    return False
                return solve(curr[word[ind]], ind + 1)
        return solve(self.trie, 0)


worddict = WordDictionary()
worddict.addWord('a')
worddict.search('.')
