class Solution:
    def longestOnes(self, nums, k: int) -> int:
        res, n = 0, len(nums)

        def solve(i, rem):
            if i >= n or rem == 0:
                return value(nums)
            flip, dont = 0, 0
            if not nums[i]:
                nums[i] = 1
                flip = solve(i + 1, rem - 1)
                nums[i] = 0
            dont = solve(i + 1, rem)
            return max(flip, dont)

        solve(0, k)
        return res