class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j, res, carry = len(a) - 1, len(b) - 1, False
        while i >= 0 and j >= 0:
            if a[i] == '1' and b[j] == '1':
                if carry:
                    res = '1' + res
                else:
                    res = '0' + res
                    carry = True
            elif a[i] == '1' or b[j] == '1':
                if carry:
                    res = '0' + res
                else:
                    res = '1' + res
            else:
                if carry:
                    res = '1' + res
                else:
                    res = '0' + res

        if carry:
            res = '1' + res
        return res


print(Solution().addBinary(a = "11", b = "1"))