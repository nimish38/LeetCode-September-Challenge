class ProductOfNumbers:

    def __init__(self):
        self.nums, self.prev = [], 1

    def add(self, num: int) -> None:
        if num == 0:
            self.nums = [0] * (len(self.nums) + 1)
            self.prev = 1
        else:
            self.nums.append(num * self.prev)
            self.prev = self.nums[-1]

    def getProduct(self, k: int) -> int:
        n = len(self.nums)
        if self.nums[n - k] == 0:
            return 0
        den = n - k - 1
        if den < 0 or self.nums[den] == 0:
            return self.nums[-1]
        return self.nums[-1] // self.nums[den]


productOfNumbers = ProductOfNumbers()
productOfNumbers.add(0)
productOfNumbers.add(0)
productOfNumbers.add(9)
print(productOfNumbers.getProduct(3))
productOfNumbers.add(8)
productOfNumbers.add(3)
productOfNumbers.add(8)
print(productOfNumbers.getProduct(5))
print(productOfNumbers.getProduct(4))
print(productOfNumbers.getProduct(6))
productOfNumbers.add(8)
productOfNumbers.add(8)