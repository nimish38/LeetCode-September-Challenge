import heapq
class MedianFinder:
    def __init__(self):
        self.min_heap, self.max_heap = [], []

    def addNum(self, num: int) -> None:
        if len(self.min_heap) == len(self.max_heap):
            heapq.heappush(self.max_heap, -1 * num)
        else:
            heapq.heappush(self.min_heap, num)

    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            return (self.max_heap[0] + self.min_heap[0]) / -2
        else:
            return -1 * self.max_heap[0]

# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
print(obj.findMedian())
obj.addNum(3)
print(obj.findMedian())
