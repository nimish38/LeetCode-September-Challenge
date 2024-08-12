class Solution:
    def solve(self, board) -> None:
        m, n = len(board), len(board[0])

        for i in range(1, n - 1):
            for j in [0, m - 1]:
                dfs(j, i)

        for i in range(m):
            for j in [0, n - 1]:
                dfs(i, j)

        return board