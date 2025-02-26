class ProductOfNumbers:

    def __init__(self):
        self.nums, self.prev = [], 1

    def add(self, num: int) -> None:
        if num == 0:
            self.nums = [0] * (len(self.nums) + 1)
            self.prev = 1
        else:
            self.nums.append(num * self.prev)
            self.prev = num

    def getProduct(self, k: int) -> int:
        n = len(self.nums)
        if n == k:
            return self.nums[-1]
        den = self.nums[n - 1 - k]
        if den == 0:
            return self.nums[n - 1]
        return self.nums[n - 1] // den


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