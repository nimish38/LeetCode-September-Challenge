class Solution:
    def pivotIndex(self, nums):
        n = len(nums)
        leftSum, rightSum = [0]*n, [0]*n
        for i in range(1, n):
            leftSum[i] = leftSum[i - 1] + nums[i - 1]
            rightSum[n - i - 1] = rightSum[n - i] + nums[n - i]

        for i in range(n):
            if leftSum[i] == rightSum[i]:
                return i
        return -1

print(Solution().pivotIndex([2,1,-1]))