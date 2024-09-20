class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        m, n, odd = len(nums1), len(nums2), False
        if (m + n) % 2:
            odd = True

        i, j, k, last, mid = 0, 0, 0, False, 0
        while k <= m + n:
            if nums1[i] < nums2[j]:
                i += 1
                last = False
            else:
                j += 1
                last = True
            k += 1

        if last:
            mid = nums2[j - 1]
        else:
            mid = nums1[i - 1]

        if not odd:
            return (mid + min(nums2[j], nums1[i])) / 2
        return mid

