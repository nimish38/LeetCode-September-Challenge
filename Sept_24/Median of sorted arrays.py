class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        m, n, odd = len(nums1), len(nums2), False
        nums1.append(float('inf'))
        nums2.append(float('inf'))

        if (m + n) % 2:
            odd = True

        i, j, k = 0, 0, 0
        idx1 = (m + n) // 2
        idx2 = idx1 - 1
        mid1, mid2 = -1, -1
        while k < idx1:
            if nums1[i] < nums2[j]:
                if k == idx2:
                    mid2 = nums1[i]
                i += 1
            else:
                if k == idx2:
                    mid2 = nums2[j]
                j += 1
            k += 1

        mid1 = min(nums1[i], nums2[j])
        if not odd:
            return (mid1 + mid2) / 2
        return mid1

print(Solution().findMedianSortedArrays(nums1 = [1,3], nums2 = [2,4,5]))