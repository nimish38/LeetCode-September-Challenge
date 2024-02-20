class Solution:
    def findDifference(self, nums1, nums2):
        res, nums1, nums2 = [], set(nums1), set(nums2)
        res.append(list(nums1 - nums2))
        res.append(list(nums2 - nums1))
        return res

print(Solution().findDifference([1,2,3,3], [1,1,2,2]))