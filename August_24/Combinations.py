class Solution:
    def combine(self, n: int, k: int):
        res = []
        def solve(curr, combo):
            if len(combo) == k:
                res.append(combo)
                return
            for i in range(curr + 1, n + 1):
                combo.append(i)
                solve(curr + 1, list(combo))
                combo.pop()

        solve(0, [])
        return res

print(Solution().combine(n = 4, k = 2))