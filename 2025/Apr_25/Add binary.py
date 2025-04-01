class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j, res, carry = len(a) - 1, len(b) - 1, '', 0
        while i >= 0 and j >= 0:
            val = int(a[i]) + int(b[j]) + carry
            res = str(val % 2) + res
            if val > 1:
                carry = 1
            else:
                carry = 0
            i -= 1
            j -= 1

        while i >= 0:
            val = int(a[i]) + carry
            res = str(val % 2) + res
            if val > 1:
                carry = 1
            else:
                carry = 0
            i -= 1

        while j >= 0:
            val = int(b[j]) + carry
            res = str(val % 2) + res
            if val > 1:
                carry = 1
            else:
                carry = 0
            j -= 1

        if carry:
            return '1' + res
        return res