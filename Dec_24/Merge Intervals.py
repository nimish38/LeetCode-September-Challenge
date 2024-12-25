class Solution:
    def merge(self, intervals):
        res, j = [], 1
        currStart, currEnd = intervals[0]
        while j < len(intervals):
            nextStart, nextEnd = intervals[j]
            if currEnd >= nextStart:
                currEnd = nextEnd
                j += 1
            else:
                res.append([currStart, currEnd])
                currStart, currEnd = intervals[j]
                j += 1
        return res
