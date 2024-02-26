class RecentCounter:

    def __init__(self):
        self.req = []

    def ping(self, t: int) -> int:
        cnt = 1
        for i in range(len(self.req) - 1, -1, -1):
            print(t - self.req[i])
            if t - self.req[i] <= 3000:
                cnt += 1
            else:
                break
        self.req.append(t)
        return cnt

# Your RecentCounter object will be instantiated and called as such:
obj = RecentCounter()
print([obj.ping(1), obj.ping(100), obj.ping(3001), obj.ping(3002)])

