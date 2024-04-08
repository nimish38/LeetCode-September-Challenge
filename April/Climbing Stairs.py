class Solution:
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        for i in range(2, n):
            cost[i] += min(cost[i - 1], cost[i - 2])
        return min(cost[-1], cost[-2])

print(Solution().minCostClimbingStairs(cost = [1,100,1,1,1,100,1,1,100,1]))