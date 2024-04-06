class Solution:
    def combinationSum3(self, k: int, n: int):
        if n > 45:
            return []

        def backtrack(start, curr_sum, k, combo):
            if k == 0:
                if curr_sum == n:
                    res.append(list(combo))
                return

            if start < 10:
                combo.append(start)
                backtrack(start + 1, curr_sum + start, k - 1, combo)
                combo.pop()
                backtrack(start + 1, curr_sum, k, combo)

        res = []
        backtrack(1, 0, k, [])
        return res

print(Solution().combinationSum3(k = 9, n = 45))