class Solution(object):
    def pacificAtlantic(self, heights):
        m, n, res = len(heights), len(heights[0]), []
        pacific, atlantic = [[0] * n for _ in range(m)], [[0] * n for _ in range(m)]

        def dfs(i, j, arr):
            if arr[i][j]:
                return
            arr[i][j] = 1
            for a, b in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                x, y = i + a, j + b
                if 0 <= x < m and 0 <= y < n and not arr[x][y] and heights[x][y] >= heights[i][j]:
                    dfs(x, y, arr)

        for i in range(m):
            dfs(i, 0, pacific)
            dfs(i, n - 1, atlantic)
        for j in range(n):
            dfs(0, j, pacific)
            dfs(m - 1, j, atlantic)
        for i in range(m):
            for j in range(n):
                if pacific[i][j] and atlantic[i][j]:
                    res.append([i, j])
        return res

print(Solution().pacificAtlantic(heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))