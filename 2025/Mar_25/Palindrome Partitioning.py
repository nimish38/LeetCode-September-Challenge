class Solution:
    def partition(self, s: str):
        n, res = len(s), []

        def solve(idx, curr):
            if idx >= n:
                res.append(curr)
                return
            for i in range(idx, n):
                presemt = s[idx: i]
                if presemt == presemt[::-1]:
                    curr.append(presemt)
                    solve(i + 1, curr)
                    curr.pop()
        solve(0, [])
        return res