class Solution:
    def candy(self, ratings):
        n = len(ratings)
        L2R = [1] * n
        # check left neightbor
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                L2R[i] = max(L2R[i], L2R[i - 1] + 1)
        # check right neighbor
            if ratings[n - i - 1] > ratings[n - i]:
                L2R[n - i - 1] = max(L2R[n - i - 1], L2R[n - i] + 1)
        return sum(L2R)

print(Solution().candy(ratings = [1,3,4,5,2]))