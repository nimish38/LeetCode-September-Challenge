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


        if checkRow() and checkCol() and checkBox():
            return True
        return False