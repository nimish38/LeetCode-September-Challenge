class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        m, n = len(nums1), len(nums2)
        nums1 += nums2
        nums1.sort()
        if (m + n) % 2:
            return nums1[(m + n) // 2]
        else:
            return (nums1[(m + n) // 2] + nums1[((m + n) // 2) - 1]) / 2


print(Solution().findMedianSortedArrays(nums1 = [1,2], nums2 = [3,4]))