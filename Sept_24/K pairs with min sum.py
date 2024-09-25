import heapq
class Solution:
    def kSmallestPairs(self, nums1, nums2, k: int):
        res, i, j = [], 0, 0

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                res.append([nums1[i], nums2[j]])

        res.sort(key=lambda x: sum(x))
        return res[:k]

print(Solution().kSmallestPairs(nums1 = [1,7,11], nums2 = [2,4,6], k = 3))