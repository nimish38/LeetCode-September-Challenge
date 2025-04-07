class WordDictionary:

    def __init__(self):
        self.tree = {}

    def addWord(self, word: str) -> None:
        curr = self.tree
        for c in word:
            if c not in curr:
                curr[c] = {}
            curr = curr[c]
        curr['*'] = True

    def search(self, word: str) -> bool:
        k = len(word)
        def solve(ind, dic):
            if ind == k:
                if '*' in dic:
                    return True
                return False
            if word[ind] == '.':
                for char in dic:
                    if char != '*' and solve(ind + 1, dic[char]):
                        return True
                return False
            else:
                if word[ind] not in dic:
                    return False
                return solve(ind + 1, dic[word[ind]])
            
        return solve(0, self.tree)
