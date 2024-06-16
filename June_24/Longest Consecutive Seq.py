class Solution:
    def longestConsecutive(self, nums) -> int:
        nums.sort()
        cnt, res = 1, -1
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] == 1:
                cnt += 1
            else:
                res = max(res, cnt)
                cnt = 1
        return res

print(Solution().longestConsecutive())