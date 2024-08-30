class Solution:
    def combinationSum(self, candidates, target: int):
        ans, path = [], []

        def backtrack(total, start_index):
            if total > target:
                return

            if total == target:
                ans.append(path[:])
                return

            for i in range(start_index, len(candidates)):
                if total + candidates[i] > target:
                    break

                total += candidates[i]
                path.append(candidates[i])
                backtrack(total, i)
                total -= candidates[i]
                path.pop()

        candidates.sort()
        backtrack(0, 0)
        return ans

print(Solution().combinationSum(candidates = [2,3,6,7], target = 7))