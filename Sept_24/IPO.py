import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits, capital) -> int:
        pairs, heap, i = [], [], 0
        for i in range(len(capital)):
            pairs.append((capital[i], profits[i]))
        pairs.sort()
        i = 0
        while k > 0:
            while i < len(capital) and pairs[i][0] <= w:
                heapq.heappush(heap, pairs[i][1])
                i += 1

            heapq._heapify_max(heap)
            w += heapq._heappop_max(heap)
            k -= 1
        return w


print(Solution().findMaximizedCapital(k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]))

