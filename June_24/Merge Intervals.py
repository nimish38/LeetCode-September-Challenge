import operator
class Solution:
    def merge(self, intervals):
        if len(intervals) < 2:
            return intervals

        intervals = sorted(intervals, key=operator.itemgetter(1, 0))
        res, i, j, start = [], 0, 1, intervals[0][0]
        while j < len(intervals):
            if intervals[j][0] <= intervals[i][1]:
                start = min(start, intervals[j][0])
                i += 1
                j += 1
            else:
                res.append([start, intervals[j - 1][1]])
                start, i, j = intervals[j][0], j, j + 1
        res.append([start, intervals[j - 1][1]])
        return res

print(Solution().merge(intervals = [[1,4],[2,3]]))