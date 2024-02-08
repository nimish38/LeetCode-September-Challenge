class Solution:
    def productExceptSelf(self, nums):
        prefixProd, suffixProd = 1, 1
        res = [1]*len(nums)
        for i in range(1, len(nums)):
            prefixProd *= nums[i-1]
            res[i] *= prefixProd
            suffixProd *= nums[len(nums) - i]
            res[len(nums) - i - 1] *= suffixProd
        return res

a= Solution()
print(a.productExceptSelf([1,2,3,4,5]))