import random


class Solution:

    def __init__(self, w):
        self.buckets, self.val = [], 0
        for v in w:
            self.buckets.append(self.val + v)
            self.val = v

    def pickIndex(self) -> int:
        def findBucket(v):
            if v < self.buckets[0]:
                return 0
            l, r = 0, len(self.buckets)
            m = (l + r) // 2
            while l < r:
                if self.buckets[m] < v:
                    l = m + 1
                elif self.buckets[m] == v or self.buckets[m - 1] < v <= self.buckets[m]:
                    return m
                else:
                    r = m - 1

        randomval = random.randrange(0, self.val)
        return findBucket(randomval)


obj = Solution(w=[1, 3])
print(obj.pickIndex())
print(obj.pickIndex())
print(obj.pickIndex())