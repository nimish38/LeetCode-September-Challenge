class Solution:
    def dfs(self, i, j, board, curr):
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0] or board[i][j] not in curr):
            return
        if '*' in curr:
            self.res.append(curr['*'])
        board[i][j] = '$'
        neigh = [(-1, 0),(1, 0),(0, -1),(0, 1)]
        for dx, dy in neigh:
            self.dfs(i + dx, j + dy, board, curr[board[i][j]])


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
                self.dfs(i, j, board, self.trie)
        return self.res

    