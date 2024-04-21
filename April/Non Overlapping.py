class Solution:
    def eraseOverlapIntervals(self, intervals):
        if len(intervals) < 2:
            return 0
        intervals.sort()
        i, j, cnt = 0, 1, 0

        while j < len(intervals):
            curr_start, curr_end, next_start, next_end = intervals[i][0], intervals[i][1], intervals[j][0], intervals[j][1]
            if curr_end > next_start:
                if curr_end > next_end:
                    cnt += 1
                    i = j
                else:
                    cnt += 1
            else:
                i = j
            j += 1

        return cnt

print(Solution().eraseOverlapIntervals(intervals = [[1,2],[2,3],[3,4],[1,3]]))





