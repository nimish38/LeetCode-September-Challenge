class Solution:
    def minSubArrayLen(self, target: int, nums) -> int:
        n = len(nums)
        for leng in range(1, n):
            for i in range(n - leng):
                if i == 0:
                    curr = sum[i: i + leng]
                else:
                    curr = curr + nums[i + leng - 1] - nums[i - 1]
                if curr >= target:
                    return leng

        

