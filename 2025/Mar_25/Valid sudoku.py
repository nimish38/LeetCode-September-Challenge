class Solution:
    def isValidSudoku(self, board) -> bool:

        def checkRow():
            for row in range(9):
                seen = {}
                for col in range(9):
                    if board[row][col] != '.':
                        if board[row][col] in seen:
                            return False
                        seen[board[row][col]] = 1
            return True

        def checkCol():
            for col in range(9):
                seen = {}
                for row in range(9):
                    if board[row][col] != '.':
                        if board[row][col] in seen:
                            return False
                        seen[board[row][col]] = 1
            return True

        def checkBox():
            for i in range(0, 9, 3):
                for j in range(0, 9, 3):
                    rowStart, rowEnd, colStart, colEnd, seen = i, i + 3, j, j + 3, {}
                    for row in range(rowStart, rowEnd):
                        for col in range(colStart, colEnd):
                            if board[row][col] != '.':
                                if board[row][col] in seen:
                                    return False
                                seen[board[row][col]] = 1
            return True

        if checkRow() and checkCol() and checkBox():
            return True
        return False


print(Solution().isValidSudoku(board =
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","5",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))