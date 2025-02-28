import random


class Solution:

    def __init__(self, w):
        self.weights = w

    def pickIndex(self) -> int:
        return random.randrange(0, len(self.weights))


obj = Solution(w=[1, 3])
print(obj.pickIndex())
print(obj.pickIndex())
print(obj.pickIndex())