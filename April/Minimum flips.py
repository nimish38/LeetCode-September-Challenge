class Solution:
    def minFlips(self, a: int, b: int, c: int):
        a, b, c = bin(a)[2:], bin(b)[2:], bin(c)[2:]
        appen_len = max(len(a), len(b), len(c))

        a = ('0' * (appen_len - len(a))) + a
        b = ('0' * (appen_len - len(b))) + b
        c = ('0' * (appen_len - len(c))) + c

        cnt = 0
        for i in range(appen_len):
            if c[i] == '1':
                if a[i] == '0' and b[i] == '0':
                    cnt += 1
            else:
                if a[i] == '1' and b[i] == '1':
                    cnt += 2
                elif a[i] == '1' or b[i] == '1':
                    cnt += 1
        return cnt

print(Solution().minFlips(a = 1, b = 2, c = 3))