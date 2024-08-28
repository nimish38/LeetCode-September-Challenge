class Solution:
    def combine(self, n: int, k: int):
        res = []
        def solve(curr, combo):
            if len(combo) == k:
                res.append(combo)
                return
            for i in range(curr, n + 1):
                combo.append(curr)
                solve(curr + 1, combo)
                combo.pop()

        solve(1, [])
        return res