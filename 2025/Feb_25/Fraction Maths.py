from fractions import Fraction


class Solution:
    def fractionAddition(self, expression: str) -> str:
        res, num, den, sign, i = 0, 0, 0, 1, 0
        if expression[0] != '-':
            num, den = int(expression[0]), int(expression[2])
            res += (num / den)
            i = 3
        while i < len(expression):
            if expression[i] == '-':
                sign = -1
            else:
                sign = 1
            num, den = int(expression[i + 1]), int(expression[i + 3])
            res += (num / den) * sign
            i += 4
        res = str(Fraction(res).limit_denominator())
        if res.count('/') == 0:
            res += '/1'
        return res

print(Solution().fractionAddition(expression = "1/3-1/2"))
