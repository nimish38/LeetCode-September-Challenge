class Solution:
    def solveSudoku(self, board) -> None:
        n = 9
        # Hash sets for tracking used numbers
        rows = [set() for _ in range(n)]
        cols = [set() for _ in range(n)]
        boxes = [set() for _ in range(n)]

        empty_cells = []

        # Prepopulate sets and find empty cells
        for r in range(n):
            for c in range(n):
                if board[r][c] == ".":
                    empty_cells.append((r, c))
                else:
                    num = int(board[r][c])
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[(r // 3) * 3 + (c // 3)].add(num)

        def solve(index):
            if index == len(empty_cells):
                return True

            row, col = empty_cells[index]
            box_id = (row // 3) * 3 + (col // 3)

            for num in range(1, 10):
                if num not in rows[row] and num not in cols[col] and num not in boxes[box_id]:
                    board[row][col] = str(num)
                    rows[row].add(num)
                    cols[col].add(num)
                    boxes[box_id].add(num)

                    if solve(index + 1):
                        return True

                    # Backtrack
                    board[row][col] = "."
                    rows[row].remove(num)
                    cols[col].remove(num)
                    boxes[box_id].remove(num)

            return False

        solve(0)
        print(board)


Solution().solveSudoku(board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],
                        ["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],
                        [".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]])