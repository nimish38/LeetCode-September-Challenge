import heapq
from collections import Counter


class Solution(object):
    def topKFrequent(self, nums, k):
        c, arr = Counter(nums), []
        for key in c:
            val = c[key]
            if len(arr) < k:
                heapq.heappush(arr, (val, key))
            else:
                heapq.heappushpop(arr, (val, key))
        return [x[1] for x in arr]

print(Solution().topKFrequent(nums = [1,1,1,2,2,3], k = 2))