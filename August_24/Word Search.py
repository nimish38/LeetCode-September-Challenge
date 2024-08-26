class Solution:
    def dfs(self, i, j, board, curr):
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] not in curr:
            return
        if board[i][j] in curr and '*' in curr[board[i][j]]:
            self.res.append(curr[board[i][j]]['*'])
        key = board[i][j]
        board[i][j] = '$'
        neigh = [(-1, 0),(1, 0),(0, -1),(0, 1)]
        for dx, dy in neigh:
            if i + dx >= 0 and i + dx < len(board) and j + dy >= 0 and j + dy < len(board[0]) and key in curr:
                self.dfs(i + dx, j + dy, board, curr[key])


    def findWords(self, board, words):
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
                    self.dfs(i, j, board, self.trie)
        return self.res

print(Solution().findWords(board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]))