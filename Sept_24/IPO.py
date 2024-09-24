import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits, capital) -> int:
        pairs, heap, i = [], [], 0
        for i in range(len(capital)):
            if capital[i] == 0:
                pairs.append((capital[i], profits[i]))
        pairs.sort()
        i = 0
        while k > 0:
            while i < len(capital) and pairs[i][0] <= w:
                heapq.heappush(heap, pairs[i][1])
                i += 1

            w += heapq._heappop_max(heap)
            k -= 1
        return w


print(Solution().findMaximizedCapital(k = 3, w = 0, profits = [1,2,3], capital = [0,1,2]))

