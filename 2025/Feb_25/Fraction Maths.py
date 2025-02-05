import math
class Solution:
    def fractionAddition(self, expression: str) -> str:
        num, den, i = 0, 1, 0
        while i < len(expression):
            numer, denom = '', ''
            while expression[i] != '/':
                numer += expression[i]
                i += 1
            i += 1
            while i < len(expression) and expression[i] not in ['+', '-']:
                denom += expression[i]
                i += 1
            numer, denom = int(numer), int(denom)
            num = (num * denom) + (den * numer)
            den = den * denom
        gcd = abs(math.gcd(num, den))
        return str(num // gcd) + '/' + str(den // gcd)


print(Solution().fractionAddition(expression = "-1/2+1/2+1/3"))
