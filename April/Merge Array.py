class Solution:
    def merge(self, nums1, m, nums2, n):
        i, j, ins = m - 1, n - 1, m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[ins] = nums1[i]
                i -= 1
                ins -= 1
            else:
                nums1[ins] = nums2[j]
                j -= 1
                ins -= 1
        return nums1

print(Solution().merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3))


