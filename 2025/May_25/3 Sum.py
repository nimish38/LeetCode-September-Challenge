class Solution:
    def threeSum(self, nums):
        res, n = [], len(nums)
        nums.sort()
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target, j, k = -1 * nums[i], i + 1, n - 1
            while j < k:
                val = nums[j] + nums[k]
                if val == target:
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while k > j and nums[k] == nums[k - 1]:
                        k -= 1
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                elif val < target:
                    j += 1
                else:
                    k -= 1
        return res

print(Solution().threeSum(nums = [2,-3,0,-2,-5,-5,-4,1,2,-2,2,0,2,-4,5,5,-10]))