class Solution:
    def candy(self, ratings):
        n = len(ratings)
        L2R, R2L = [1] * n, [1] * n
        # check left neightbor
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                L2R[i] = L2R[i - 1] + 1
        # check right neighbor
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                R2L[i] = R2L[i + 1] + 1
        cnt = 0
        for i in range(n):
            cnt += max(L2R[i], R2L[i])
        return cnt

print(Solution().candy(ratings = [1,0,2]))