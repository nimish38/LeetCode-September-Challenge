import copy
class Solution:
    def dfs(self, i, j, bo, curr):
        if i < 0 or i >= len(bo) or j < 0 or j >= len(bo[0]) or bo[i][j] not in curr:
            return
        if bo[i][j] in curr and '*' in curr[bo[i][j]]:
            self.res.add(curr[bo[i][j]]['*'])
        key = bo[i][j]
        bo[i][j] = '$'
        neigh = [(-1, 0),(1, 0),(0, -1),(0, 1)]
        for dx, dy in neigh:
            if i + dx >= 0 and i + dx < len(bo) and j + dy >= 0 and j + dy < len(bo[0]) and key in curr:
                new_bo = copy.deepcopy(bo)
                self.dfs(i + dx, j + dy, new_bo, curr[key])
        bo[i][j] = key


    def findWords(self, board, words):
        self.trie = {}
        for word in words:
            curr = self.trie
            for char in word:
                if char not in curr:
                    curr[char] = {}
                curr = curr[char]
            curr['*'] = word


        self.res = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in self.trie:
                    self.dfs(i, j, board, self.trie)
        return list(self.res)

print(Solution().findWords(board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]))