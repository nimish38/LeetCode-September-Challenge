class Solution:
    def combinationSum(self, candidates, target: int):
        res = []

        def solve(curr, rem, ind):
            if rem == 0:
                res.append(curr)
                return

            for i in range(ind, len(candidates)):
                if candidates[i] <= rem:
                    curr.append(candidates[i])
                    solve(list(curr), rem - candidates[i], i)
                    curr.pop()

        solve([], target, 0)
        return res

print(Solution().combinationSum(candidates = [2,3,6,7], target = 7))