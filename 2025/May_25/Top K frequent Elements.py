import heapq
from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        counter = Counter(nums)
        queue = []
        for v, f in counter.items():
            heapq.heappush(queue, (f, v))
            if len(queue) > k:
                heapq.heappop(queue)

        results = [v for f, v in queue]
        return results

print(Solution().topKFrequent(nums = [1,1,1,2,2,3], k = 2))
