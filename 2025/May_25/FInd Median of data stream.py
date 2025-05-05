import heapq

class MedianFinder:

    def __init__(self):
        self.min, self.max, self.even = [], [], True

    def addNum(self, num: int) -> None:
        if not self.max or num < self.max[0] * -1:
            heapq.heappush(self.max, num * -1)
            while len(self.max) - len(self.min) > 1:
                heapq.heappush(self.min, heapq.heappop(self.max) * -1)
        else:
            heapq.heappush(self.min, num)
            while len(self.min) - len(self.max) > 0:
                heapq.heappush(self.max, heapq.heappop(self.min) * -1)
        self.even = not self.even

    def findMedian(self) -> float:
        val = 0
        if self.min:
            val = self.min[0]
        if self.even:
            return ((self.max[0] * -1) + val) / 2
        return self.max[0] * -1


medianFinder = MedianFinder()
medianFinder.addNum(1)
medianFinder.addNum(2)
print(medianFinder.findMedian())
medianFinder.addNum(3)
print(medianFinder.findMedian())