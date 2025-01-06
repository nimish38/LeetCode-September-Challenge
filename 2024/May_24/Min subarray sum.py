class Solution:
    def minSubArrayLen(self, target, nums):
        i, j, minwindow = 0, 0, len(nums)
        curr_sum, match_flag = 0, False
        while j < len(nums):
            curr_sum += nums[j]
            while curr_sum >= target:
                match_flag = True
                minwindow = min(minwindow, j - i + 1)
                curr_sum -= nums[i]
                i += 1
            j += 1
        if not match_flag:
            return 0
        return minwindow

print(Solution().minSubArrayLen(target = 7, nums = [2,3,1,2,4,3]))




