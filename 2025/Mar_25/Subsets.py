class Solution:
    def subsets(self, nums):
        res = [[]]
        for num in nums:
            for subset in res[:]:
                res.append(subset + [num])
        return res


print(Solution().subsets(nums = [1,2,3]))