class Solution(object):
    def subsets(self, nums):
        n, res = len(nums), []

        def solve(ind, curr):
            if ind >= n:
                res.append(list(curr))
                return
            curr.append(nums[ind])
            solve(ind + 1, curr)
            curr.pop()
            solve(ind + 1, curr)

        solve(0, [])
        return res

print(Solution().subsets(nums = [1,2,3]))