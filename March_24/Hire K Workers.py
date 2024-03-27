import heapq
class Solution:
    def totalCost(self, costs, k, candidates):
        cost, first, last = 0, costs[:candidates], costs[len(costs) - candidates:]
        i, j = candidates - 1, len(costs) - candidates
        for var in range(j, i + 1):
            last.pop(0)
        heapq.heapify(first)
        heapq.heapify(last)
        while k > 0:
            if len(last) == 0 or  first[0] <= last[0]:
                cost += heapq.heappop(first)
                if i < j:
                    i += 1
                    heapq.heappush(first, costs[i])
            else:
                cost += heapq.heappop(last)
                if j > i:
                    j -= 1
                    heapq.heappush(last, costs[j])
            k -= 1
        return cost

print(Solution().totalCost(costs = [1,2,4,1], k = 4, candidates = 3))