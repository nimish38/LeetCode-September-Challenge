class Solution:
    def minSubArrayLen(self, target: int, nums) -> int:
        n = len(nums)
        for leng in range(1, n + 1):
            curr = 0
            for i in range(n - leng + 1):
                if i == 0:
                    curr = sum(nums[: leng])
                else:
                    curr = curr + nums[i + leng - 1] - nums[i - 1]
                if curr >= target:
                    return leng
        return 0


print(Solution().minSubArrayLen(target = 15, nums = [1,2,3,4,5]))

