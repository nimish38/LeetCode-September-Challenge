class Solution:
    def combine(self, n: int, k: int):
        res = []
        def solve(curr, combo):
            if len(combo) == k:
                res.append(combo)
                return
            if curr > n:
                return
            combo.append(curr)
            solve(curr + 1, list(combo))
            combo.pop()
            solve(curr + 1, list(combo))

        solve(1, [])
        return res

print(Solution().combine(n = 4, k = 2))