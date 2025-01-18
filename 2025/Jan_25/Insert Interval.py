class Solution:
    def insert(self, intervals, newInterval):
        if not intervals:
            return [newInterval]
        i, n, newStart, newEnd, res = 0, len(intervals), newInterval[0], newInterval[1], []
        if newEnd < intervals[0][0]:
            return [newInterval] + intervals
        while i < n and intervals[i][1] < newStart:
            res.append(intervals[i])
            i += 1
        if i < n:
            newStart = min(newStart, intervals[i][0])
        while i < n and intervals[i][0] <= newEnd:
            i += 1
        newEnd = max(newEnd, intervals[i - 1][1])
        res.append([newStart, newEnd])
        res.extend(intervals[i:])
        return res


print(Solution().insert(intervals = [[1,5]], newInterval = [0,0]))

