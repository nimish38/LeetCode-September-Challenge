class Solution:
    def fractionAddition(self, expression: str) -> str:
        res, num, den, sign, i = 0, 0, 1, 1
        if expression[0] == '-':
            sign, num, den = -1, expression[1], expression[3]
            res += (num / den) * sign
            i = 4
        while i < len(expression):
            if expression[i] == '-':
                sign = -1
            else:
                sign = 1
            num, den = expression[i + 1], expression[i + 3]
            res += (num / den) * sign
            i += 4
        return res

    
