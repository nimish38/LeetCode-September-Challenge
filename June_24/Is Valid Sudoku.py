class Solution:
    def isValidSudoku(self, board):
        for row in board:
            num = 0
            curr = set()
            for ele in  row:
                if ele != '.':
                    num += 1
                    curr.add(ele)
            if num != len(curr):
                return False
            
        for i in range(9):
            num = 0
            curr = set()
            for j in range(9):
                if board[j][i] != '.':
                    num += 1
                    curr.add(board[j][i])
            if num != len(curr):
                return False

        def Traverse(sr, er, sc, ec):
            num, curr = 0, set()
            for i in range(sr, er + 1):
                for j in range(sc, ec + 1):
                    if board[i][j] != '.':
                        num += 1
                        curr.add(board[i][j])
                if num != len(curr):
                    return False
            return True
                    
        for start_row in range(0, 9, 3):
            end_row = start_row + 2
            for start_col in range(0, 9, 3):
                end_col = start_col + 2
                if not Traverse(start_row, end_row, start_col, end_col):
                    return False
        return True

print(Solution().isValidSudoku(board =
[[".",".",".",".","5",".",".","1","."],
 [".","4",".","3",".",".",".",".","."],
 [".",".",".",".",".","3",".",".","1"],
 ["8",".",".",".",".",".",".","2","."],
 [".",".","2",".","7",".",".",".","."],
 [".","1","5",".",".",".",".",".","."],
 [".",".",".",".",".","2",".",".","."],
 [".","2",".","9",".",".",".",".","."],
 [".",".","4",".",".",".",".",".","."]]))