class Solution:
    def merge(self, intervals):
        if len(intervals) < 2:
            return intervals

        intervals = sorted(intervals, key=lambda x: x[1])
        res, i, j, start = [], 0, 1, intervals[0][0]
        while j < len(intervals):
            if intervals[j][0] <= intervals[i][1]:
                i += 1
                j += 1
            else:
                res.append([start, intervals[j - 1][1]])
                start, i, j = intervals[j][0], j, j + 1
        res.append([start, intervals[j - 1][1]])
        return res

print(Solution().merge(intervals = [[1,3],[2,6],[8,10],[10,18], [11,21]]))