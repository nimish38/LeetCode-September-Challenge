class Solution:
    def merge(self, intervals):
        res, j = [], 1
        intervals.sort(key=lambda x: x[0])
        currStart, currEnd = intervals[0]
        while j < len(intervals):
            nextStart, nextEnd = intervals[j]
            if currEnd >= nextStart:
                currEnd = max(currEnd, nextEnd)
                j += 1
            else:
                res.append([currStart, currEnd])
                currStart, currEnd = intervals[j]
                j += 1
        res.append([currStart, currEnd])
        return res


print(Solution().merge(intervals = [[1,3],[2,6],[8,10],[15,18]]))