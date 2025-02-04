class Solution:
    def fractionAddition(self, expression: str) -> str:
        res, num, den, sign, i = 0, 0, 0, 1, 1
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
        return res


print(Solution().fractionAddition(expression = "1/3-1/2"))
