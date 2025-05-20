class Solution(object):
    def combinationSum(self, candidates, target):
        res, n = [], len(candidates)

        def solve(ind, curr, add):
            if ind >= n:
                return
            if add == target:
                res.append(curr.copy())
                return
            for i in range(ind, n):
                if add + candidates[i] <= target:
                    curr.append(candidates[i])
                    solve(i, curr, add + candidates[i])
                    curr.pop()

        solve(0, [], 0)
        return res

print(Solution().combinationSum(candidates = [2,3,5], target = 8))