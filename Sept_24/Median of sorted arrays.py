class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        m, n, odd = len(nums1), len(nums2), False
        nums1.append(float('inf'))
        nums2.append(float('inf'))

        if (m + n) % 2:
            odd = True

        i, j, k, nums = 0, 0, 0, []
        while k < (m + n) // 2:
            if nums1[i] < nums2[j]:
                nums.append(nums1[i])
                i += 1
            else:
                nums.append(nums2[j])
                j += 1
            k += 1
        nums.append(min(nums1[i], nums2[j]))
        if not odd:
            return (nums[-1] + nums[-2]) / 2
        return nums[-1]

print(Solution().findMedianSortedArrays(nums1 = [1,3], nums2 = [2,4,5]))