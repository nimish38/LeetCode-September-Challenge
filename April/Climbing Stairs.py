class Solution:
    def minCostClimbingStairs(self, cost):

        def climb(ind, curr_cost):
            if ind == n and curr_cost < self.res:
                self.res = curr_cost
                return
            elif ind == n - 1 and curr_cost + cost[ind] < self.res:
                self.res = curr_cost + cost[ind]
                return

            if ind < n - 1:
                climb(ind + 1, curr_cost + cost[ind])
                climb(ind + 2, curr_cost + cost[ind])

        n = len(cost)
        self.res = float('inf')
        climb(0, 0)
        climb(1, 0)
        return self.res

print(Solution().minCostClimbingStairs(cost = [1,100,1,1,1,100,1,1,100,1]))