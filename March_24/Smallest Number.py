import heapq
class SmallestInfiniteSet:
    def __init__(self):
        self.cnt, self.added = 1, heapq

    def popSmallest(self) -> int:
        if len(self.added) > 0 and self.added[0] < self.cnt:
            return self.added.heappop()
        self.cnt += 1
        return self.cnt - 1

    def addBack(self, num: int) -> None:
        if self.cnt > num:
            self.added.heappush(num)

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)