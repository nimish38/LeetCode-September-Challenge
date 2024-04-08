class Solution:
    def minCostClimbingStairs(self, cost):
        def climb(ind):
            if ind >= n:
                return 0
            if memorise[ind] != -1:
                return memorise[ind]
            memorise[ind] = cost[ind] + min(climb(ind + 1), climb(ind + 2))
            return memorise[ind]

        n = len(cost)
        memorise = [-1]*(n + 1)
        return min(climb(0), climb(1))

print(Solution().minCostClimbingStairs(cost = [1,100,1,1,1,100,1,1,100,1]))