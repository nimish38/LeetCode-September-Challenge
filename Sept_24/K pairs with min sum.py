import heapq
class Solution:
    def kSmallestPairs(self, nums1, nums2, k: int):
        res = []
        heapq.heapify(nums1)
        heapq.heapify(nums2)

        for _ in range(k):
            a, b = heapq.heappop(nums1), heapq.heappop(nums2)
            res.append([a, b])
            if nums1[0] < nums2[0]:
                heapq.heappush(nums2, b)
            else:
                heapq.heappush(nums1, a)
        return res