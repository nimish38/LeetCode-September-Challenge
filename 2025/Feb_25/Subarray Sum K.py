class Solution:
    def subarraySum(self, nums, k: int) -> int:
        cnt, n = 0, len(nums)
        for length in range(1, n):
            summ = 0
            for i in range(n - length + 1):
                if i == 0:
                    summ = sum(nums[i : i + length])
                else:
                    summ = summ - nums[i - 1] + nums[i + length - 1]
                if summ == k:
                    cnt += 1
        return cnt


print(Solution().subarraySum(nums = [1,2,3], k = 3))
