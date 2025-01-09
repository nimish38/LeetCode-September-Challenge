class Solution:
    def findWords(self, board, words):
        res, m, n = [], len(board), len(board[0])

        def solve(i, j, str):
            if not str:
                return True
            letter = board[i][j]
            board[i][j] = '#'
            up = down = left = right = False
            if i > 0 and board[i - 1][j] == str[0]:
                up = solve(i - 1, j, str[1:])
            if i < m - 1 and board[i + 1][j] == str[0]:
                down = solve(i + 1, j, str[1:])
            if j > 0 and board[i][j - 1] == str[0]:
                left = solve(i, j - 1, str[1:])
            if j < n - 1 and board[i][j + 1] == str[0]:
                right = solve(i, j + 1, str[1:])
            board[i][j] = letter
            return up or down or left or right

        for word in words:
            for i in range(m):
                for j in range(n):
                    if board[i][j] == word[0] and solve(i, j, word[1:]):
                        res.append(word)

        return res