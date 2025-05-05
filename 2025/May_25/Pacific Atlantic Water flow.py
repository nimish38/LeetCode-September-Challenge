from collections import deque

class Solution:
    def pacificAtlantic(self, heights):
        m, n, pac, atl = len(heights), len(heights[0]), [], []
        pac = [[False] * n for _ in range(m)]
        atl = [[False] * n for _ in range(m)]

        def dfs(a, b, ocean):
            ocean[a][b], nei = True, [(0, 1), (0, -1),(1, 0),(-1, 0)]
            for x, y in nei:
                r, c = a + x, b + y
                if 0 <= r < m and 0 <= c < n and not ocean[r][c] and heights[r][c] >= heights[a][b]:
                    dfs(r, c, ocean)

        for i in range(n):
            dfs(0, i, pac)
            dfs(m - 1, i, atl)

        for i in range(m):
            dfs(i, 0,  pac)
            dfs(i, n - 1, atl)

        res = []
        for i in range(m):
            for j in range(n):
                if pac[i][j] and atl[i][j]:
                    res.append([i, j])
        return res


print(Solution().pacificAtlantic(heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))

