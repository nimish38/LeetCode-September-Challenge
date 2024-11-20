class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        def solve(zero, one, consCnt, consEle):
            if zero == 0 and one == 0:
                return 1
            res = 0
            if zero > 0:
                if consEle == 0 and consCnt <= limit:
                    res += solve(zero - 1, one, consCnt + 1, 0)
                else:
                    res += solve(zero - 1, one, 1, 0)

            if one > 0:
                if consEle == 1 and consCnt <= limit:
                    res += solve(zero, one - 1, consCnt + 1, 1)
                else:
                    res += solve(zero, one - 1, 1, 1)

            return res
        return solve(zero, one - 1, 1, 1) + solve(zero - 1, one, 1, 0)

print(Solution().numberOfStableArrays(zero = 1, one = 1, limit = 2))