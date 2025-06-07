class Solution(object):
    def permuteUnique(self, nums):
        n, res = len(nums), []
        def solve(ind):
            if ind == n:
                res.append(list(nums))
                return
            seen = set()
            for i in range(ind, n):
                if nums[i] not in seen:
                    seen.add(nums[i])
                    nums[i], nums[ind] = nums[ind], nums[i]
                    solve(ind + 1)
                    nums[i], nums[ind] = nums[ind], nums[i]
        solve(0)
        return res

print(Solution().permuteUnique([1, 1, 2]))