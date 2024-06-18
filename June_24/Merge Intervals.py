class Solution:
    def merge(self, intervals):
        if len(intervals) < 2:
            return intervals
        intervals.sort(key=lambda x: x[1])
        res, i, j = [], 0, 1
        while j < len(intervals):
            if intervals[j][0] <= intervals[i][1]:
                j += 1
            else:
                res.append([intervals[i][0], intervals[j - 1][1]])
                i, j = j, j + 1
        res.append([intervals[i][0], intervals[j - 1][1]])
        return res

print(Solution().merge(intervals = [[1,3],[8,10],[2,6],[15,18]]))