class Solution:
    def subsets(self, nums):
        n, res = len(nums), []

        def solve(curr, ind):
            if ind >= n:
                res.append(list(curr))
                return
            curr.append(nums[ind])
            solve(curr, ind + 1)
            curr.pop()
            solve(curr, ind + 1)

        solve([], 0)
        return res


print(Solution().subsets(nums = [1,2,3]))