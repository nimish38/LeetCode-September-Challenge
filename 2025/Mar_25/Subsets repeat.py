class Solution(object):
    def subsets(self, nums):
        n = len(nums)

        def solve(ind):
            if ind >= n:
                return [[]]
            curr = solve(ind + 1)
            res = list(curr)
            for combo in curr:
                x = list(combo)
                x.append(nums[ind])
                res.append(x)
            return res

        return solve(0)

print(Solution().subsets(nums = [1,2,3]))