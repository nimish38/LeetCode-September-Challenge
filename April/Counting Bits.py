class Solution:
    def countBits(self, n: int):
        res = [0]
        for i in range(1, n + 1):
            res.append(str(bin(i)).count('1'))
        return res

print(Solution().countBits(5))