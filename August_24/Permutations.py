class Solution:
    def permute(self, nums):
        res, n = [], len(nums)

        def solve(combo, rem):
            if len(combo) == n:
                res.append([*combo])
                return
            for i in range(len(rem)):
                combo.append(rem[i])
                temp = rem[:i] + rem[i + 1:]
                solve(combo, temp)
                combo.pop()

        solve([], nums)
        return res

print(Solution().permute(nums = [1,2,3]))