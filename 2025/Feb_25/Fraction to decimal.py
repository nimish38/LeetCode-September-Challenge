class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        res, remainder = '', {}
        if numerator < denominator:
            res += '0.'
        else:
            res += str(numerator // denominator) + '.'
            numerator = numerator % denominator
        numerator *= 10
        while numerator > 0 and numerator not in remainder:
            quo = numerator // denominator
            remainder[quo] = 1
            if numerator < denominator:
                numerator *= 10
            else:
                numerator %= denominator
        res += ''.join(str(x) for x in remainder.keys())
        return res


print(Solution().fractionToDecimal(numerator = 1, denominator = 2))

