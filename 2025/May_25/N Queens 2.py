class Solution(object):
    def totalNQueens(self, n):
        self.res, col, diag, anti = 0, set(), set(), set()

        def solve(row):
            if row == n:
                self.res += 1
            for c in range(n):
                if c not in col and row + c not in diag and row - c not in anti:
                    col.add(c)
                    diag.add(row + c)
                    anti.add(row - c)
                    solve(row + 1)
                    col.remove(c)
                    diag.remove(row + c)
                    anti.remove(row - c)
        solve(0)
        return self.res

print(Solution().totalNQueens(n = 4))