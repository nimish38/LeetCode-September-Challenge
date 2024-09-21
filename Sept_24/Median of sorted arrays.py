class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        m, n = len(nums1), len(nums2)
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)

        start, end = 0, m
        while start <= end:
            Px = (start + end) // 2
            Py = ((m + n + 1) // 2) - Px

            if Px == 0:
                x1 = float('-inf')
            else:
                x1 = nums1[Px - 1]
            if Py == 0:
                x2 = float('-inf')
            else:
                x2 = nums2[Py - 1]

            if Px == m:
                x3 = float('inf')
            else:
                x3 = nums1[Px]
            if Py == n:
                x4 = float('inf')
            else:
                x4 = nums2[Py]


            if x1 <= x4 and x2 <= x3:
                if (m + n) % 2:
                    return max(x1, x2)
                return (max(x1, x2) + min(x3, x4)) / 2
            
            elif x1 > x4:
                end = Px - 1
            else:
                start = Px + 1 


print(Solution().findMedianSortedArrays(nums1 = [1,3], nums2 = [2,4,5]))