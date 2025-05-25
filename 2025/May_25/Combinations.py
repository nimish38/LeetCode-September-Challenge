class Solution(object):
    def combine(self, n, k):
        end, res = n - k + 1, []
        def solve(ind, combo):
            if len(combo) == k:
                res.append(list(combo))
                return
            if ind > n or ind > end and len(combo) == 0:
                return
            combo.append(ind)
            solve(ind + 1, combo)
            combo.pop()
            solve(ind + 1, combo)
        solve(1, [])
        return res

print(Solution().combine(n = 4, k = 2))