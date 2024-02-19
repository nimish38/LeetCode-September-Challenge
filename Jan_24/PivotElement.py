class Solution:
    def pivotIndex(self, nums):
        leftSum, rightSum = 0, sum(nums)
        for idx, ele in enumerate(nums):
            rightSum -= ele
            if rightSum == leftSum:
                return idx
            leftSum += ele
        return -1

print(Solution().pivotIndex([2,1,-1]))