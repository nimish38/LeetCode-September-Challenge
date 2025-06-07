class Solution(object):
    def permute(self, nums):
        res, n = [], len(nums)
        def solve(ind):
            if ind == n:
                res.append(list(nums))
                return
            for i in range(ind, n):
                nums[i], nums[ind] = nums[ind], nums[i]
                solve(ind + 1)
                nums[i], nums[ind] = nums[ind], nums[i]
        solve(0)
        return res

print(Solution().permute([1, 2, 3]))