import random, bisect


class Solution:

    def __init__(self, w):
        self.buckets = [0]
        for v in w:
            self.buckets.append(self.buckets[-1] + v)

    def pickIndex(self) -> int:
        def findBucket(v):
            if v < self.buckets[0]:
                return 0
            l, r = 0, len(self.buckets) - 1

            while l <= r:
                m = (l + r) // 2
                if self.buckets[m] < v:
                    l = m + 1
                elif self.buckets[m] == v or self.buckets[m - 1] <= v < self.buckets[m]:
                    return m
                else:
                    r = m - 1

        randomval = random.randint(1, self.buckets[-1])
        # ind = findBucket(randomval)
        ind = bisect.bisect_left(self.buckets, randomval)
        return ind - 1


obj = Solution(w=[1, 3])
print(obj.pickIndex())
print(obj.pickIndex())
print(obj.pickIndex())
print(obj.pickIndex())
print(obj.pickIndex())