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
                self.intervals.append((startTime, endTime))
                return True
            else:
                return False
