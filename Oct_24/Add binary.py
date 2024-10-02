class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j, res, carry = len(a) - 1, len(b) - 1, '', False
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
                    carry = False
                else:
                    res = '0' + res

            i -= 1
            j -= 1

        while i >= 0:
            if a[i] == '1':
                if carry:
                    res = '0' + res
                    carry = True
                else:
                    res = '1' + res
            else:
                if carry:
                    res = '1' + res
                    carry = False
                else:
                    res = '0' + res
            i -= 1

        while j >= 0:
            if b[j] == '1':
                if carry:
                    res = '0' + res
                    carry = True
                else:
                    res = '1' + res
            else:
                if carry:
                    res = '1' + res
                    carry = False
                else:
                    res = '0' + res
            j -= 1


        if carry:
            res = '1' + res
        return res


print(Solution().addBinary(a = "1010", b = "1011"))