class Solution:
    def productExceptSelf(self, nums):
        cnt = nums.count(0)
        if cnt > 1:
            return [0]*len(nums)
        else:
            prod = 1
            for val in nums:
                if val:
                    prod *= val
            if cnt == 1:
                idx = nums.index(0)
                nums = [0] * (len(nums) - 1)
                nums.insert(idx, prod)
                return nums
            else:
                for i in range(len(nums)):
                    if nums[i]:
                        nums[i] = prod // nums[i]
                    else:
                        nums[i] = prod
                return nums

a= Solution()
print(a.productExceptSelf([-1,1,0,-3,3]))