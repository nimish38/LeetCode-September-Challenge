class ProductOfNumbers:

    def __init__(self):
        self.nums, self.prev = [], 1

    def add(self, num: int) -> None:
        if num == 0:
            self.nums = []
        elif len(self.nums) == 0:
            self.nums.append(num)
        else:
            self.nums.append(self.nums[-1] * num)

    def getProduct(self, k: int) -> int:
        if k > len(self.nums):
            return 0
        elif k == len(self.nums):
            return self.nums[-1]
        return self.nums[-1] // self.nums[len(self.nums) - k - 1]


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