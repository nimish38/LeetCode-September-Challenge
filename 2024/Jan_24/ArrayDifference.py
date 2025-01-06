class Solution:
    def findDifference(self, nums1, nums2):
        res, elem = [[], []], {}

        for num in nums1:
            if num not in elem:
                elem[num] = False

        for num in nums2:
            if num in elem:
                elem[num] = True
            if num not in res[1]:
                res[1].append(num)

        for val in elem:
            if not elem[val]:
                res[0].append(val)

        return res



print(Solution().findDifference([1,2,3], [2,4,6]))