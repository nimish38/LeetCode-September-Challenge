class Solution:
    def permute(self, nums):
        res, n = [], len(nums)

        def swap(ind):
            if ind >= n:
                res.append(list(nums))
                return
            for i in range(ind, n):
                nums[i], nums[ind] = nums[ind], nums[i]
                swap(ind + 1)
                nums[i], nums[ind] = nums[ind], nums[i]
        swap(0)
        return res


print(Solution().permute(nums = [1,2,3]))