class Solution:
    def convert(self, s: str, numRows: int) -> str:
        zigzag = [''] * numRows

        inc, cnt = True, 0
        for char in s:
            if inc:
                zigzag[cnt] += char
                cnt += 1
                if cnt == numRows:
                    inc = False
                    cnt -= 2
            else:
                zigzag[cnt] += char
                cnt -= 1
                if cnt < 0:
                    inc = True
                    cnt += 2

        return ''.join(zigzag)

print(Solution().convert(s = "PAYPALISHIRING", numRows = 4))