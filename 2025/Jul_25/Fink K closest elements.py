import heapq

class Solution(object):
    def findClosestElements(self, arr, k, x):
        heap, res = [], []
        for num in arr:
            if len(heap) == k:
                heapq.heappushpop(heap, (-abs(num - x), -num))
            else:
                heapq.heappush(heap, (-abs(num - x), -num))
        for diff, val in heap:
            res.append(-val)
        return sorted(res)

print(Solution().findClosestElements(arr = [1,2,3,4,5], k = 4, x = 3))