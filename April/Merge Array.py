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

        if j >= 0:
            for k in range(j + 1):
                nums1[k] = nums2[k]

        print(nums1)

print(Solution().merge(nums1 = [2,0], m = 1, nums2 = [1], n = 1))


