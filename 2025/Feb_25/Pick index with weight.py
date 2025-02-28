import random


class Solution:

    def __init__(self, w):
        self.buckets, self.val = [], 0
        for v in w:
            self.buckets.append(self.val + v)
            self.val = v

    def pickIndex(self) -> int:
        randomval = random.randint % self.val
        return findBucket(randomval)


obj = Solution(w=[1, 3])
print(obj.pickIndex())
print(obj.pickIndex())
print(obj.pickIndex())