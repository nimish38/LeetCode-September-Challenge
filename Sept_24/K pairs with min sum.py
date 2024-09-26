import heapq
class Solution:
    def kSmallestPairs(self, nums1, nums2, k: int):
        res, i, j = [], 0, 0

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                sum, pair = nums1[i] + nums2[j], [nums1[i], nums2[j]]
                heapq.heappush(res, (-1 * sum, pair))
                if len(res) > k:
                    heapq.heappop(res)
        result = []
        for _ in range(k):
            result.append(heapq.heappop(res)[1])
        return result[::-1]

print(Solution().kSmallestPairs(nums1 = [1,7,11], nums2 = [2,4,6], k = 3))