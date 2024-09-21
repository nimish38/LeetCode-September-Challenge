class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        m, n = len(nums1), len(nums2)
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)

        start, end = 0, m
        while start <= end:
            Px = (start + end) // 2
            Py = ((m + n + 1) // 2) - Px

            x1 = nums1[Px - 1]
            x2 = nums2[Py - 1]

            x3 = nums1[Px]
            x4 = nums2[Py]

print(Solution().findMedianSortedArrays(nums1 = [1,3], nums2 = [2,4,5]))