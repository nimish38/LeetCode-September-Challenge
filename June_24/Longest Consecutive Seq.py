class Solution:
    def longestConsecutive(self, nums) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        cnt, res = 1, -1
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] == 1:
                cnt += 1
            else:
                res = max(res, cnt)
                cnt = 1
        return max(res, cnt)

print(Solution().longestConsecutive(nums = [0,3,7,2,5,8,4,6,0,1]))