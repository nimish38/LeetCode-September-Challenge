class Solution:
    def jump(self, nums):
        if len(nums) == 1:
            return 0
        i, cnt = 0, 0
        while i < len(nums) - 1:
            cnt += 1
            if i + nums[i] >= len(nums) - 1:
                return cnt
            maxval, maxind = -1, -1
            for j in range(i + 1, i + nums[i] + 1):
                if j + nums[j] >= len(nums) - 1:
                    return cnt + 1
                if nums[j] >= maxval:
                    maxval, maxind = nums[j], j
            i = maxind
        return cnt

print(Solution().jump([1,2]))