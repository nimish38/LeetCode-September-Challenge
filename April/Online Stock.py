class StockSpanner:
    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        cnt, i = 1, len(self.stack) - 1
        while i > 0 and self.stack[i] <= price:
            cnt += 1
            i -= 1
        self.stack.append(price)
        return cnt

s = StockSpanner()
print(s.next(100))
print(s.next(80))
print(s.next(60))
print(s.next(70))
print(s.next(60))
print(s.next(75))
print(s.next(85))





