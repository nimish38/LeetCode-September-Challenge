import heapq
class Solution:
    def totalCost(self, costs, k, candidates):
        cost, first, last = 0, costs[:candidates], costs[len(costs) - candidates:]
        heapq.heapify(first)
        heapq.heapify(last)
        i, j = candidates - 1, len(costs) - candidates
        while k > 0:
            if first[0] <= last[0]:
                cost += heapq.heappop(first)
                i += 1
                heapq.heappush(first, costs[i])
            else:
                cost += heapq.heappop(last)
                j -= 1
                heapq.heappush(first, costs[j])
            k -= 1

        return cost

print(Solution().totalCost(costs = [17,12,10,2,7,2,11,20,8], k = 3, candidates = 4))