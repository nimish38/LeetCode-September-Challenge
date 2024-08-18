from collections import deque
class Solution:
    def snakesAndLadders(self, board) -> int:
        n, que = len(board), deque()
        vis = []
        for _ in range(n):
            vis.append([False]*n)
        vis[n - 1][0] = True
        que.append(1)

        

print(Solution().snakesAndLadders(board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]))