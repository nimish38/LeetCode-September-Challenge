import heapq
class SmallestInfiniteSet:
    def __init__(self):
        self.cnt, self.added = 1, []
        heapq.heapify(self.added)

    def popSmallest(self) -> int:
        if len(self.added) > 0 and self.added[0] < self.cnt:
            return heapq.heappop(self.added)
        self.cnt += 1
        return self.cnt - 1

    def addBack(self, num: int) -> None:
        if self.cnt > num:
            heapq.heappush(self.added, num)

# Your SmallestInfiniteSet object will be instantiated and called as such:
obj = SmallestInfiniteSet()
print(obj.popSmallest())
obj.addBack(1)
print(obj.popSmallest())
print(obj.popSmallest())
print(obj.popSmallest())
print(obj.popSmallest())
obj.addBack(3)
print(obj.popSmallest())
print(obj.popSmallest())