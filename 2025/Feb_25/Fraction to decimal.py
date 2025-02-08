class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        res, remainder, quotients = '', {}, set()
        if numerator < denominator:
            res += '0.'
        else:
            res += str(numerator // denominator) + '.'
            numerator = numerator % denominator
        remainder[numerator] = 1
        numerator *= 10
        while numerator > 0 and numerator not in remainder:
            quo, rem = numerator // denominator, numerator % denominator
            remainder[rem] = 1
            quotients.add(quo)
            numerator = rem * 10
        if numerator == 0:
            res += ''.join(str(x) for x in quotients)
        else:
            val = ''.join(str(x) for x  in quotients)
            res += '(' + val + ')'
        return res


print(Solution().fractionToDecimal(numerator = 4, denominator = 333))

