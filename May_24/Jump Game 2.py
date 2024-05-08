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
                if j + nums[j] >= maxval:
                    maxval, maxind = j + nums[j], j
            i = maxind
        return cnt

print(Solution().jump([9,8,2,2,0,2,2,0,4,1,5,7,9,6,6,0,6,5,0,5]))