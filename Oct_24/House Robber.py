class Solution:
    def rob(self, nums) -> int:
        n = len(nums)

        def solve(ind, curr):
            if ind >= n:
                return curr
            incl = solve(ind + 2, curr + nums[ind])
            excl = solve(ind + 1, curr)
            return max(incl, excl)

        return solve(0, 0)

print(Solution().rob(nums = [2,7,9,3,1]))