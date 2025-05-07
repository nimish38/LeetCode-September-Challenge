class Solution:
    def eraseOverlapIntervals(self, intervals) -> int:
        if len(intervals) == 1:
            return 0
        intervals.sort(key = lambda x: x[1])
        i, j, cnt = 0, 1, 0
        while j < len(intervals):
            end_first, begin_second = intervals[i][1], intervals[j][0]
            if end_first > begin_second:
                cnt += 1
                j += 1
            else:
                i, j = j, j + 1
        return cnt

