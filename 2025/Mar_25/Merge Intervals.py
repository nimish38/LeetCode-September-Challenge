class Solution:
    def merge(self, intervals):
        intervals.sort()
        currStart, currEnd, i, res = intervals[0][0], intervals[0][1], 1, []

        while i < len(intervals):
            newStart, newEnd = intervals[i]
            if currEnd >= newStart:
                currStart, currEnd = min(currStart, newStart), max(currEnd, newEnd)
            else:
                res.append([currStart, currEnd])
                currStart, currEnd = newStart, newEnd
            i += 1
        res.append([currStart, currEnd])
        return res


print(Solution().merge(intervals = [[1,4],[4,5]]))