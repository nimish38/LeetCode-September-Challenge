class Solution(object):
    def solveNQueens(self, n):
        board, res = [['.'] * n for _ in range(n)], []
        cols, diag, anti = set(), set(), set()

        def makeAns(chess):
            ans = []
            for i in range(n):
                ans.append(''.join(chess[i]))
            res.append(ans)

        def solve(row):
            if row >= n:
                makeAns(board)
                return

            for c in range(n):
                d, a = row + c, row - c
                if c not in cols and d not in diag and a not in anti:
                    board[row][c] = 'Q'
                    cols.add(c)
                    diag.add(d)
                    anti.add(a)
                    solve(row + 1)
                    board[row][c] = '.'
                    cols.remove(c)
                    diag.remove(d)
                    anti.remove(a)
        solve(0)
        return res

print(Solution().solveNQueens(n = 4))