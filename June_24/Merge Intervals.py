class Solution:
    def merge(self, intervals):
        if len(intervals) < 2:
            return intervals
        res, i, j = [], 0, 1
        while j < len(intervals):
            if intervals[j][0] <= intervals[i][1]:
                j += 1
            else:
                res.append([intervals[i][0], intervals[j - 1][1]])
                i, j = j, j + 1
        res.append([intervals[i][0], intervals[j - 1][1]])
        return res