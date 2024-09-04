class Solution:
    def exist(self, board:, word: str) -> bool:
        m, n = len(board), len(board[0])

        def search(row, col, ind):
            if ind == len(word):
                return True
            if m <= row < 0 or n <= col < 0 or board[i][j] != word[ind]:
                return False
            dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dx, dy in dir:
                if search(row + dx, col + dy, ind + 1):
                    return True
            return False


        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if search(i, j, 1):
                        return True
        return False