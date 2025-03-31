class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i, j, carry, res = len(num1) - 1, len(num2) - 1, False, ''
        while i >= 0 and j >= 0:
            val = int(num1[i]) + int(num2[j])
            if carry:
                val += 1
                carry = False
            if val > 9:
                carry = True
                res = str(val % 10) + res
            else:
                res = str(val) + res
            i -= 1
            j -= 1
        while i >= 0:
            val = int(num1[i])
            if carry:
                val += 1
                carry = False
            if val > 9:
                carry = True
                res = str(val % 10) + res
            else:
                res = str(val) + res
            i -= 1
        while j >= 0:
            val = int(num2[j])
            if carry:
                val += 1
                carry = False
            if val > 9:
                carry = True
                res = str(val % 10) + res
            else:
                res = str(val) + res
            j -= 1
        if carry:
            return '1' + res
        return res


print(Solution().addStrings(num1 = "11", num2 = "123"))