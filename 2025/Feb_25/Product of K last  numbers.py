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


productOfNumbers = ProductOfNumbers()
productOfNumbers.add(3)
productOfNumbers.add(0)
productOfNumbers.add(2)
productOfNumbers.add(5)
productOfNumbers.add(4)
print(productOfNumbers.getProduct(2))
print(productOfNumbers.getProduct(3))
print(productOfNumbers.getProduct(4))
productOfNumbers.add(8)
print(productOfNumbers.getProduct(2))