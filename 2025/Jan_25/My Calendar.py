class MyCalendar:

    def __init__(self):
        self.intervals = []

    def book(self, startTime: int, endTime: int) -> bool:
        if not self.intervals:
            self.intervals.append((startTime, endTime))
            return True
        i, n = 0, len(self.intervals)
        while i < n and self.intervals[i][1] <= startTime:
            i += 1
        if i == n:
            self.intervals.append((startTime, endTime))
            return True
        else:
            if self.intervals[i][0] >= endTime:
                self.intervals.insert(i, (startTime, endTime))
                return True
            return False


cal = MyCalendar()
ints, res = [[10,20],[15,25],[20,30]], []
for s, e in ints:
    res.append(cal.book(startTime=s, endTime=e))
print(res)
