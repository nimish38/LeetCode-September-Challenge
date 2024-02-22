class Solution:
    def equalPairs(self, grid):
        cnt = 0
        for i in range(len(grid)):
            strcol = []
            for j in range(len(grid)):
                strcol.append(grid[j][i])
            cnt += grid.count(strcol)
        return cnt

print(Solution().equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]))


