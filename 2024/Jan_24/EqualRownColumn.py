from collections import Counter
class Solution:
    def equalPairs(self, grid):
        # * is to unpack each list
        transpose = Counter(zip(*grid))
        # map is used to convert list to tuples as it is accepted by Counter
        grid = Counter(map(tuple,grid))
        return sum(transpose[t] * grid[t] for t in transpose)

print(Solution().equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]))


