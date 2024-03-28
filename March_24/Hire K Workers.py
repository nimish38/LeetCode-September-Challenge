import heapq
class Solution:
    def totalCost(self, costs, k, candidates):
        i, j = candidates - 1, max(candidates, len(costs) - candidates)
        cost, first, last = 0, costs[:candidates], costs[j:]
        heapq.heapify(first)
        heapq.heapify(last)
        while k > 0:
            if len(first) > 0 and (len(last) == 0 or first[0] <= last[0]):
                cost += heapq.heappop(first)
                if i < j - 1:
                    i += 1
                    heapq.heappush(first, costs[i])
            else:
                cost += heapq.heappop(last)
                if j > i + 1:
                    j -= 1
                    heapq.heappush(last, costs[j])
            k -= 1
        return cost

print(Solution().totalCost(costs = [57,33,26,76,14,67,24,90,72,37,30], k = 11, candidates = 2))