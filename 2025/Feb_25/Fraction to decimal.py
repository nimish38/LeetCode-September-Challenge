class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        res, remainder = '', {}
        if numerator < denominator:
            res += '0.'
        else:
            res += str(numerator // denominator) + '.'
            numerator = numerator % denominator

        while numerator > 0 and numerator not in remainder:
            remainder[numerator] = 1
            if numerator < denominator:
                numerator *= 10
            else:
                numerator //= denominator
                numerator %= denominator
        res += ''.join(remainder.values())


