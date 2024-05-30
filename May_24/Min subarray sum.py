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
        if minwindow == len(nums) and curr_sum < target:
            return 0
        return minwindow

print(Solution().minSubArrayLen(target = 7, nums = [2,3,1,2,4,3]))




