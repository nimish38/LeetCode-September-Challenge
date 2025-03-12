class Solution:
    def countOrders(self, n: int) -> int:
        cnt = 1
        for i in range(2, n):
            spaces = (n - 1) * 2 + 1
            cnt *= spaces * (spaces + 1) // 2
        return cnt
