class Solution(object):
    def subsetsWithDup(self, nums):
        n, res = len(nums), []
        nums.sort()

        def solve(ind, curr):
            if ind >= n:
                res.append(list(curr))
                return
            curr.append(nums[ind])
            solve(ind + 1, curr)
            curr.pop()
            while ind < n - 1 and nums[ind] == nums[ind + 1]:
                ind += 1
            solve(ind + 1, curr)

        solve(0, [])
        return res

print(Solution().subsetsWithDup(nums = [1,2,2]))