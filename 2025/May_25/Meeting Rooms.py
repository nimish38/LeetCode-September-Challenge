class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def canAttendMeetings(self, intervals) -> bool:
        if len(intervals) < 2:
            return True
        intervals.sort(key = lambda x: x.start)
        for i in range(1, len(intervals)):
            prev_end, curr_start = intervals[i - 1][1], intervals[i][0]
            if curr_start < prev_end:
                return False
        return True