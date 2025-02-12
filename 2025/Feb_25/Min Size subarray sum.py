class Solution:
    def minSubArrayLen(self, target: int, nums) -> int:
        n = len(nums)
        for leng in range(1, n):
            curr = 0
            for i in range(n - leng + 1):
                if i == 0:
                    curr = sum(nums[: leng])
                else:
                    curr = curr + nums[i + leng - 1] - nums[i - 1]
                if curr >= target:
                    return leng
        return 0


print(Solution().minSubArrayLen(target = 7, nums = [2,3,1,2,4,3]))

