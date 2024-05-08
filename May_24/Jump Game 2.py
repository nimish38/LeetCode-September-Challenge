class Solution:
    def jump(self, nums):
        if len(nums) == 1:
            return 0
        i, cnt = 0, 0
        while i < len(nums) - 1:
            maxval, j = -1, i + 1
            while j < i + nums[i]:
                if j >= len(nums) - 1:
                    break
                maxval = max(maxval, j)
                j += 1
            i = j
            cnt += 1
        return cnt

print(Solution().jump(nums = [2,3,1,1,4]))