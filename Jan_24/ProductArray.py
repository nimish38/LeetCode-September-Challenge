class Solution:
    def productExceptSelf(self, nums):
        prefixProd = [1]*len(nums)
        suffixProd = [1]*len(nums)
        res = []
        cnt = 1
        sf = 1
        for i in range(1, len(nums)):
            cnt *= nums[i-1]
            prefixProd[i] = cnt

            sf *= nums[len(nums) - i]
            suffixProd[len(nums) - i - 1] = sf

        for i in range(len(nums)):
            res.append(prefixProd[i] * suffixProd[i])

        return res

a= Solution()
print(a.productExceptSelf([1,2,3,4,5]))