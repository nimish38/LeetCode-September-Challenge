class Solution:
    def jump(self, nums):
        if len(nums) == 1:
            return 0
        i, cnt = 0, 0
        while i < len(nums) - 1:
            maxval, maxind, j = -1, -1, i + 1
            while j < i + nums[i] + 1:
                if j >= len(nums) - 1:
                    return cnt + 1
                if nums[j] > maxval:
                    maxval, maxind = nums[j], j
                j += 1
            i = maxind
            cnt += 1
        return cnt

print(Solution().jump(nums = [2,3,0,1,4]))