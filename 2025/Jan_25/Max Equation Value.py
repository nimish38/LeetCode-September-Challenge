import heapq

class Solution:
    def findMaxValueOfEquation(self, points, k: int) -> int:
        j, n, best, pq = 0, len(points), float('-inf'), []
        heapq.heapify(pq)
        for i in range(n):
            while pq and points[i][0] - pq[0][1] > k:
                heapq.heappop(pq)
            if pq:
                best = max(best, points[i][0] + points[i][1] + pq[0][0])
            heapq.heappush((points[i][1] - points[i][0], points[i][0]))

        return best


print(Solution().findMaxValueOfEquation(points = [[0,0],[3,0],[9,2]], k = 3))