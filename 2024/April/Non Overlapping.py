class Solution:
    def eraseOverlapIntervals(self, intervals):
        intervals.sort(key= lambda x: x[1] )
        res = 0
        end = intervals[0][1]

        for s, e in intervals[1:]:
            if s < end:
                res += 1
            else:
                end = e
        return res

print(Solution().eraseOverlapIntervals(intervals = [[2,12],[3,7],[9,12]]))





