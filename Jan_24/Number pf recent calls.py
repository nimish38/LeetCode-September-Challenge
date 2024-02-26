class RecentCounter:

    def __init__(self):
        self.req = []
        self.front, self.back = 0, -1

    def ping(self, t: int) -> int:
        self.back += 1
        self.req.append(t)

        while self.front <= self.back and self.req[self.back] - self.req[self.front] > 3000:
            self.front += 1

        return self.back - self.front + 1


# Your RecentCounter object will be instantiated and called as such:
obj = RecentCounter()
print([obj.ping(1), obj.ping(100), obj.ping(3001), obj.ping(3002)])

