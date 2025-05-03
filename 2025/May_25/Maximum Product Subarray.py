class Solution:
    def maxProduct(self, nums) -> int:
        best, pre, suff, n = float('-inf'), 1, 1, len(nums) - 1
        for i in range(len(nums)):
            if pre == 0:
                pre = 1
            if suff == 0:
                suff = 1
            pre *= nums[i]
            suff *= nums[n - i]
            best = max(best, pre, suff)
        return best