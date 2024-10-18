class Solution:
    def rob(self, nums) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        amt = [-1]*(n + 1)
        amt[0], amt[1] = 0, nums[0]

        for i in range(2, n + 1):
            amt[i] = max(amt[i - 1], amt[i - 2] + nums[i - 1])
        return amt[n]


print(Solution().rob(nums = [2,7,9,3,1]))