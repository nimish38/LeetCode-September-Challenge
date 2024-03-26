import heapq
from collections import defaultdict
class Solution:
    def maxScore(self, nums1, nums2, k):
        maximum, curr, nums2Sorted = 0, 0, defaultdict()

        for i in range(len(nums2)):
            nums2Sorted[nums2[i]] = nums1[i]

        sorted(nums2Sorted, reverse=True)
        i, minheap, values = 0, [], nums2Sorted.values()
        while i < k:
            heapq.heappush(minheap, nums2Sorted[i])
            curr += nums2Sorted[i]
            i += 1

        maximum = curr * values[k - 1]
        while i < len(nums2):
            curr -= heapq.heappop(minheap)
            heapq.heappush(minheap, nums2Sorted[i])
            curr += nums2Sorted[i]

            if curr * values[i] > maximum:
                maximum = curr * values[i]

        return maximum






