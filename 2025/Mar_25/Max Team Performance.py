import heapq


class Solution:
    def maxPerformance(self, n: int, speed, efficiency, k: int) -> int:
        combo, curr, bestsum, heap = [], 0, 0, []
        for i in range(n):
            combo.append((efficiency[i], speed[i]))
        combo.sort(key=lambda x: x[0], reverse=True)
        for i in range(n):
            if len(heap) >= k:
                curr -= heapq.heappop(heap)
            curr += combo[i][1]
            heapq.heappush(heap, combo[i][1])
            bestsum = max(bestsum, curr * combo[i][0])
        return bestsum % (10**9 + 7)


print(Solution().maxPerformance(n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 2))

