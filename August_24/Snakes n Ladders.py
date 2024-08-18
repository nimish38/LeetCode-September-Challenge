from collections import deque
class Solution:
    def snakesAndLadders(self, board) -> int:
        n, que = len(board), deque()

        def getCords(num):
            row_top = (num - 1) // n
            row_bottom = n - 1 - row_top
            col_num = (num - 1) % n
            if n % 2 == row_bottom % 2:
                col_num = n - 1 - col_num
            return row_bottom, col_num

        vis, steps = [], 0
        for _ in range(n):
            vis.append([False]*n)
        vis[n - 1][0] = True
        que.append(1)

        while que:
            lvl = len(que)
            for _ in range(lvl):
                cell = que.popleft()
                if cell == n*n:
                    return steps
                for i in range(1, 7):
                    val = cell + i
                    if val < n*n:
                        row, col = getCords(val)
                        if vis[row][col]:
                            continue
                        if board[row][col] == -1:
                            que.append(val)
                        else:
                            que.append(board[row][col])
                        vis[row][col] = True

            steps += 1
        return -1

print(Solution().snakesAndLadders(board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]))