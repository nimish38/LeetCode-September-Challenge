class Solution:
    def exist(self, board:, word: str) -> bool:
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if search(i, j, 1):
                        return True
        return False