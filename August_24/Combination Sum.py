class Solution:
    def combinationSum(self, candidates, target: int):
        res = []

        def solve(combo, cursum, ind):
            if cursum == target:
                res.append([*combo])
                return
            if cursum > target:
                return
            for i in range(ind, len(candidates)):
                combo.append(candidates[i])
                solve(combo, cursum + candidates[i], i)
                combo.pop()

        solve([], 0, 0)
        return res

print(Solution().combinationSum(candidates = [2,3,6,7], target = 7))