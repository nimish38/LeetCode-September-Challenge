class Solution:
    def exist(self, board, word: str):
        m, n = len(board), len(board[0])

        def search(row, col, ind):
            if ind == len(word):
                return True
            if row < 0 or row >= m or col >= n or col < 0 or board[row][col] != word[ind]:
                return False
            board[row][col] = '$'
            dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dx, dy in dir:
                if search(row + dx, col + dy, ind + 1):
                    return True
            board[row][col] = word[ind]
            return False


        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if search(i, j, 0):
                        return True
        return False

print(Solution().exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"))