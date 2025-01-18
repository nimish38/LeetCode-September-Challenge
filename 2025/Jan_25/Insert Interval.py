class Solution:
    def insert(self, intervals, newInterval):
        i, n, newStart, newEnd, res = 0, len(intervals), newInterval[0], newInterval[1], []
        while i < n and intervals[i][1] <= newStart:
            res.append(intervals[i])
            i += 1
        newStart = min(newStart, intervals[i - 1][0])
        while i < n and intervals[i][0] <= newEnd:
            i += 1
        newEnd = max(newEnd, intervals[i - 1][1])
        res.append([newStart, newEnd])
        res.extend(intervals[i :])

