import heapq

class Solution:
    def findMaxValueOfEquation(self, points, k: int) -> int:
        n, best, pq = len(points), float('-inf'), []
        for i in range(n):
            while pq and points[i][0] - pq[0][1] > k:
                heapq.heappop(pq)
            if pq:
                best = max(best, points[i][0] + points[i][1] + (-1 * pq[0][0]))
            heapq.heappush(pq, ((points[i][1] - points[i][0]) * -1, points[i][0]))
        return best


print(Solution().findMaxValueOfEquation([[-19,-12],[-13,-18],[-12,18],[-11,-8],[-8,2],[-7,12],[-5,16],[-3,9],[1,-7],[5,-4],[6,-20],[10,4],[16,4],[19,-9],[20,19]], k = 6))