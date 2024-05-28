class Solution:
    def threeSum(self, nums):
        res, n = [], len(nums)
        for i in range(len(nums) - 2):
            j, k = i + 1, n - 1
            while j < k:
                if nums[j] + nums[k] + nums[i] == 0:
                    res.append([i, j, k])
        return res

print(Solution().threeSum(nums = [-1,0,1,2,-1,-4]))
