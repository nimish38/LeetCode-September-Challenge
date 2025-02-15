import heapq


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        m, n = len(nums1), len(nums2)
        leftmax, rightmin = [], []

        make_heap(nums1, m)
        make_heap(nums2, n)

        if (m + n) % 2:
            return leftmax[0]
        else:
            return (leftmax[0] + rightmin[0]) / 2


print(Solution().findMedianSortedArrays(nums1 = [1,2], nums2 = [3,4]))