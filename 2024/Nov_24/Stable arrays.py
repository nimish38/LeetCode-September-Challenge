class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        memo = []
        for i in range(zero + 1):
            x = []
            for j in range(one + 1):
                z = []
                for k in range(limit + 1):
                    z.append([-1] * 3)
                x.append(z)
            memo.append(x)

        def solve(zero, one, consCnt, consEle):
            if zero == 0 and one == 0:
                return 1
            # print(zero, one, consCnt, consEle)
            if consEle == 2 or memo[zero][one][consCnt][consEle] == -1:
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

                memo[zero][one][consCnt][consEle] = res
            return memo[zero][one][consCnt][consEle] % mod

        mod = (10**9) + 7
        return solve(zero, one, 0, 2) % mod

print(Solution().numberOfStableArrays(zero = 1, one = 1, limit = 2))