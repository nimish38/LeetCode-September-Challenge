class Solution(object):
    def exist(self, board, word):
        m, n, t = len(board), len(board[0]), len(word)

        def checkWord(i, j , k):
            temp, board[i][j] = board[i][j], '#'
            for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                a, b = i + x, j + y
                if 0 <= a < m and 0 <= b < n and board[a][b] == word[k + 1]:
                    if k + 2 == t:
                        return True
                    elif checkWord(a, b, k + 1):
                        return True
            board[i][j] = temp
            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if t == 1:
                        return True
                    elif checkWord(i, j, 0):
                        return True
        return False


print(Solution().exist(board = [["C","A","A"],["A","A","A"],["B","C","D"]], word = "AAB"))