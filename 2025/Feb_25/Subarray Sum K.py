class Solution:
    def subarraySum(self, nums, k: int) -> int:
        cnt, n = 0, len(nums)
        for length in range(1, n - 1):
            summ = 0
            for i in range(n - i):
                if i == 0:
                    summ = sum(nums[i : i + length])
                else:
                    summ = summ - nums[i - 1] + nums[i + length]
                if summ == k:
                    cnt += 1
        return cnt
