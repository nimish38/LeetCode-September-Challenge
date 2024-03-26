import heapq
from collections import defaultdict
class Solution:
    def maxScore(self, nums1, nums2, k):
        maximum, curr, nums2Sorted = 0, 0, defaultdict()

        for i in range(len(nums2)):
            nums2Sorted[nums2[i]] = nums1[i]

        i, minheap, values = 0, [], list(nums2Sorted.keys())
        values.sort(reverse=True)
        while i < k:
            minheap.append(nums2Sorted[values[i]])
            curr += nums2Sorted[values[i]]
            i += 1

        heapq.heapify(minheap)
        maximum = curr * values[k - 1]
        while i < len(nums2):
            curr -= heapq.heappop(minheap)
            heapq.heappush(minheap, nums2Sorted[values[i]])
            curr += nums2Sorted[values[i]]
            if curr * values[i] > maximum:
                maximum = curr * values[i]
            i += 1

        return maximum

print(Solution().maxScore(nums1 = [4,2,3,1,1], nums2 = [7,5,10,9,6], k = 1))






