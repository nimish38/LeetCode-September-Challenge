class Solution(object):
    def combinationSum2(self, candidates, target):
        n, res = len(candidates), []
        candidates.sort()

        def solve(ind, curr, add):
            if add == target:
                res.append(curr.copy())
                return
            for i in range(ind, n):
                if i > ind and candidates[i] == candidates[i - 1]:
                    continue
                if add + candidates[i] > target:
                    break
                curr.append(candidates[i])
                solve(i + 1, curr, add + candidates[i])
                curr.pop()

        solve(0, [], 0)
        return res

print(Solution().combinationSum2(candidates = [10,1,2,7,6,1,5], target = 8))