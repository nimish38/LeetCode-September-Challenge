class Solution:
    def minFlips(self, a: int, b: int, c: int):
        cnt = 0
        while a > 0 and b > 0 and c > 0: 
            if c & 1 == 1:
                if a & 1 == 0 and b & 1 == 0:
                    cnt += 1
            else:
                if a & 1 == 1 and b & 1 == 1:
                    cnt += 2
                elif a & 1 == 1 or b & 1 == 1:
                    cnt += 1

            a = a >> 1
            b = b >> 1
            c = c >> 1
        return cnt

print(Solution().minFlips(a = 2, b = 6, c = 5))