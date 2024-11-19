class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        def solve(zero, one, consCnt, consEle):
            if zero == 0 and one == 0:
                return 1
            if zero > 0 and consCnt <= limit or consEle == 1:
                solve(zero - 1, one, consCnt + 1, 0)

            if one > 0 and consCnt <= limit or consEle == 0:
                solve(zero, one - 1, consCnt + 1, 1)

        return solve(zero, one - 1, 1, 1) + solve(zero - 1, one, 1, 0)