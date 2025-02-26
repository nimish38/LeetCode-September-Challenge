class ProductOfNumbers:

    def __init__(self):
        self.nums = []

    def add(self, num: int) -> None:
        self.nums.append(num)

    def getProduct(self, k: int) -> int:
        n, res = len(self.nums), 1
        for i in range(k):
            res *= self.nums[n - 1 - i]
        return res


