class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        def solve(zero, one, consCnt, consEle):
            if zero == 0 and one == 0:
                return 1
            res = 0
            if zero > 0:
                if consEle == 0 and consCnt < limit:
                    res += solve(zero - 1, one, consCnt + 1, 0)
                elif consEle == 1 or consEle == 2:
                    res += solve(zero - 1, one, 1, 0)

            if one > 0:
                if consEle == 1 and consCnt < limit:
                    res += solve(zero, one - 1, consCnt + 1, 1)
                elif consEle == 0 or consEle == 2:
                    res += solve(zero, one - 1, 1, 1)

            return res
        mod = (10**9) + 7
        return solve(zero, one, 0, 2) % mod

print(Solution().numberOfStableArrays(zero = 1, one = 1, limit = 2))