class Solution:
    def longestOnes(self, nums, k: int) -> int:
        best, zero, l, r, n = 0, 0, 0, 0, len(nums)
        while r < n:
            if not nums[r]:
                zero += 1
                while zero > k:
                    if not nums[l]:
                        zero -= 1
                    l += 1
            else:
                best = max(best, r - l + 1)
            r += 1
        return best


print(Solution().longestOnes([1,1,1,0,0,0,1,1,1,1,0], k = 2))