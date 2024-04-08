class Solution:
    def minCostClimbingStairs(self, cost):

        def climb(ind, curr_cost):
            if ind == len(cost) and curr_cost < self.res:
                res = curr_cost
                return res
            elif ind == len(cost) - 1 and curr_cost + cost[ind] < self.res:
                res = curr_cost + cost[ind]
                return res

            climb(ind + 1, curr_cost + cost[ind])
            climb(ind + 2, curr_cost + cost[ind])

        self.res = float('inf')
        climb(0, 0)
        climb(1, 0)
        return self.res

print(Solution().minCostClimbingStairs(cost = [10,15,20]))