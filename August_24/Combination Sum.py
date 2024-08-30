class Solution:
    def combinationSum(self, candidates, target: int):
        res = []

        def solve(combo, cursum):
            if cursum == target:
                res.append([*combo])
                return
            if cursum > target:
                return
            for num in candidates:
                combo.append(num)
                solve(combo, cursum + num)
                combo.pop()

        solve([], 0)
        return res
