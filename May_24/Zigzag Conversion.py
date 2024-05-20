class Solution:
    def convert(self, s: str, numRows: int) -> str:
        zigzag, n = [], len(s) // 2
        for _ in numRows:
            zigzag.append([''] * n)

        inc, cnt = True, 0
        for char in s:
            if inc:
                zigzag[cnt].append(char)
                cnt += 1
                if cnt == numRows:
                    inc = False
                    cnt -= 2
            else:
                zigzag[cnt].append(char)
                cnt -= 1
                if cnt < 0:
                    inc = True
                    cnt += 2

        res = ''
        for i in range(numRows):
            res += ''.join(zigzag[i])
        return res

