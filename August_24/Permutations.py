class Solution:
    def permute(self, nums):
        res, n = [], len(nums)

        def solve(combo, rem):
            if len(combo) == n:
                res.append([*combo])
                return
            for i in range(rem):
                combo.append(i)
                temp = rem[:i] + rem[i + 1:]
                solve(combo, temp)
                combo.pop()

        solve([], nums)
        return res