import operator
class Solution:
    def merge(self, intervals):
        if len(intervals) < 2:
            return intervals

        intervals = sorted(intervals, key=lambda x: x[0])
        res, i, j, start, end = [], 0, 1,intervals[0][0], intervals[0][1]
        while j < len(intervals):
            if intervals[j][0] <= end:
                end = max(end, intervals[j][1])
                i += 1
                j += 1
            else:
                res.append([start, end])
                start, end, i, j = intervals[j][0], intervals[j][1], j, j + 1
        res.append([start, end])
        return res

print(Solution().merge(intervals = [[2,3],[4,5],[6,7],[8,9],[1,10]]))