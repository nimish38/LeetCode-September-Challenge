class Solution:
    def permute(self, nums):
        res, n = [], len(nums)

        def solve(combo):
            if len(combo) == n:
                res.append(combo)
                return
            for i in range(n):
                if nums[i] not in combo:
                    combo.append(nums[i])
                    solve(list(combo))
                    combo.pop()
        solve([])
        return res


print(Solution().permute(nums = [1,2,3]))