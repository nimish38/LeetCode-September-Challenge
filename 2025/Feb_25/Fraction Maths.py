class Solution:
    def fractionAddition(self, expression: str) -> str:
        num, den, i = 0, 1, 0
        while i < len(expression):
            numer, denom = '', ''
            while expression[i] != '/':
                numer += expression[i]
                i += 1
            i += 1
            while expression[i] not in ['+', '-']:
                denom += expression[i]
                i += 1
            numer, denom = int(numer), int(denom)
            num = (num * denom) + (den * numer)
            den = den * denom
            i += 1
        return str(num) + '/' + str(den)


print(Solution().fractionAddition(expression = "-5/2+10/3+7/9"))
