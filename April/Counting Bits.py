class Solution:
    def countBits(self, n: int):
        res = [0]
        if n == 0:
            return res
        for i in range(1, n + 1):
            if i % 2:
                res.append(res[i // 2] + 1)
            else:
                res.append(res[i // 2])
        return res

print(Solution().countBits(5))