class Solution:
    def solve(self, board) -> None:
        m, n = len(board), len(board[0])

        def dfs(i, j):
            st = [(i, j)]
            while st:
                a, b = st.pop()
                if a < 0 or a >= m or b < 0 or b >= n or board[a][b] != 'O':
                    continue

                board[a][b] = 'V'
                st.extend([(a - 1, b), (a + 1, b), (a, b - 1), (a, b + 1)])

        for i in range(1, n - 1):
            for j in [0, m - 1]:
                if board[j][i] == 'O':
                    dfs(j, i)

        for i in range(m):
            for j in [0, n - 1]:
                if board[i][j] == 'O':
                    dfs(i, j)

        return board