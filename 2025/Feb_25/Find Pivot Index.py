class Solution:
    def pivotIndex(self, nums) -> int:
        n = len(nums)
        left, right = [0] * n, [0] * n
        for i in range(1, n):
            left[i] = left[i - 1] + nums[i - 1]
            right[n - i - 1] = right[n - i] + nums[n - i]
        for i in range(n):
            if left[i] == right[i]:
                return i
        return -1


print(Solution().pivotIndex(nums = [1,7,3,6,5,6]))