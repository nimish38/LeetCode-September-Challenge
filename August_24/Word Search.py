class Solution:
    def findWords(self, board:, words):
        self.trie = {}
        for word in words:
            curr = self.trie
            for char in word:
                if char not in curr:
                    curr[char] = {}
                curr = curr[char]
            curr['*'] = word


        self.res = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in self.trie:
                    dfs(i, j, board)

        return self.res