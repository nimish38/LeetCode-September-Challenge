class Solution:
    def isValidSudoku(self, board):
        row_set, col_set, box_set = set(), set(), set()
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    x = str(i) + '_ROW_' + str(board[i][j])
                    if x in row_set:
                        return False
                    row_set.add(x)

                    y = str(j) + '_COL_' + str(board[i][j])
                    if y in col_set:
                        return False
                    col_set.add(y)

                    z = str(i//3) + str(j//3) + '_BOX_' + str(board[i][j])
                    if z in box_set:
                        return False
                    box_set.add(z)
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