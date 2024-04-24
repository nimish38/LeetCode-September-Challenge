class StockSpanner:
    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        if self.stack and price > self.stack[-1][0]:
            cnt = self.stack[-1][1] + 1
        else:
            cnt = 1
        self.stack.append((price, cnt))
        return cnt

s = StockSpanner()
print(s.next(31))
print(s.next(41))
print(s.next(48))
print(s.next(59))
print(s.next(79))
print(s.next(75))
print(s.next(85))





