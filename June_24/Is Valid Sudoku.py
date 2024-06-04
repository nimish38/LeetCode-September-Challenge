from collections import defaultdict
class Solution:
    def isValidSudoku(board) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        grid = defaultdict(set)
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val.isalnum():
                    k = i // 3 * 3 + j // 3
                    if val in row[i] or val in col[j] or val in grid[k]:
                        return False
                    else:
                        row[i].add(val)
                        col[j].add(val)
                        grid[k].add(val)

        return True

print(Solution().isValidSudoku(board =
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))