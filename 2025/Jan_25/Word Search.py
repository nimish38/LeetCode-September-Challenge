class Solution:
    def findWords(self, board, words):
        res, m, n = [], len(board), len(board[0])
        for word in words:
            for i in range(m):
                for j in range(n):
                    if board[i][j] == word[0] and solve(i, j, word[1:]):
                        res.append(word)

        return res