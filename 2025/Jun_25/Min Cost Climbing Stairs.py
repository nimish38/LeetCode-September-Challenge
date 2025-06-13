class Solution:
    def minCostClimbingStairs(self, cost) -> int:
        n = len(cost)
        memo = [0] * (n + 1)
        for i in range(2, n + 1):
            memo[i] = min(memo[i - 2] + cost[i - 2], memo[i - 1] + cost[i - 1])
        return memo[-1]

print(Solution().minCostClimbingStairs(cost = [1,100,1,1,1,100,1,1,100,1]))