import heapq
class MedianFinder:
    def __init__(self):
        self.min_heap, self.max_heap = [], []

    def addNum(self, num: int) -> None:
        if self.max_heap and num > -1 * self.max_heap[0]:
            heapq.heappush(self.min_heap, num)
        else:
            heapq.heappush(self.max_heap, -1 * num)

        if abs(len(self.max_heap) - len(self.min_heap)) > 1:
            x = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, x * -1 )
        elif len(self.min_heap) > len(self.max_heap):
            x = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, x * -1)


    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            return ((-1 * self.max_heap[0]) + self.min_heap[0]) / 2
        else:
            return -1 * self.max_heap[0]

# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
print(obj.findMedian())
obj.addNum(3)
print(obj.findMedian())
