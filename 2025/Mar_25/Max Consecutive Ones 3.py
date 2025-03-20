class Solution:
    def longestOnes(self, nums, k: int) -> int:
        best, n = 0, len(nums)
        for i in range(n):
            zero = 0
            for j in range(i, n):
                if not nums[j]:
                    zero += 1
                if zero <= k:
                    best = max(best, j - i + 1)
                else:
                    break
        return best


print(Solution().longestOnes([1,1,1,0,0,0,1,1,1,1,0], k = 2))