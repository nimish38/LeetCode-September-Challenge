class Solution(object):
    def rob(self, nums):
        n, arr = len(nums), [0]*len(nums)
        if n < 3:
            return max(nums)

        def robbing(l, r):
            leftprev, left = nums[l], max(nums[l], nums[l + 1])
            for i in range(l + 2, r + 1):
                left, leftprev = max(left, leftprev + nums[i]), left
            return left

        return max(robbing(0, n - 2), robbing(1, n - 1))

print(Solution().rob(nums = [3,2,3]))