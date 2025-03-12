class Solution:
    def countOrders(self, n: int) -> int:
        cnt = 1
        for i in range(2, n + 1):
            spaces = (i - 1) * 2 + 1
            cnt *= spaces * (spaces + 1) // 2
        return cnt % (10**9 + 7)


print(Solution().countOrders(n = 3))