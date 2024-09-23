import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits, capital) -> int:
        for i in range(len(capital)):
            if capital[i] == 0:
                w += profits[i]
                k -= 2

        heap = []
        for i in range(len(capital)):
            if capital[i] != 0:
                heapq.heappush(heap, (profits[i], capital[i]))
        heapq._heapify_max(heap)

        while w > 0 and k > 0:
            pro, cap = heapq.heappop(heap)
            if cap <= w:
                w = w + pro - cap
                k -= 1

        return w


print(Solution().findMaximizedCapital(k = 3, w = 0, profits = [1,2,3], capital = [0,1,2]))

