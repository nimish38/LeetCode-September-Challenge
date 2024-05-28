class Solution:
    def threeSum(self, nums):
        res, n = [], len(nums)
        nums.sort()
        for i in range(n - 2):
            j, k = i + 1, n - 1
            while j < k:
                curr = nums[j] + nums[k] + nums[i]
                if curr == 0:
                    if [nums[i], nums[j], nums[k]] not in res:
                        res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                elif curr < 0:
                    j += 1
                else:
                    k -= 1
        return res

print(Solution().threeSum(nums = [-1,0,1,2,-1,-4]))
