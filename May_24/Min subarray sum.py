class Solution:
    def minSubArrayLen(self, target, nums):
        i, j, minwindow = 0, 0, len(nums)
        curr_sum = 0
        while j < len(nums):
            curr_sum += nums[j]
            while curr_sum >= target:
                minwindow = min(minwindow, j - i + 1)
                curr_sum -= nums[i]
                i += 1
            j += 1
        return minwindow

print(Solution().minSubArrayLen())




