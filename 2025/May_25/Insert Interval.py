class Solution(object):
    def insert(self, intervals, newInterval):
        if len(intervals) == 0:
            return [newInterval]
        if newInterval[1] < intervals[0][0]:
            intervals.insert(0, newInterval)

        res, ins = [], False
        for i in range(len(intervals)):
            st, end = intervals[i]
            if newInterval[0] > end:
                res.append(intervals[i])
            else:
                if newInterval[1] < st:
                    res.append(newInterval)
                    ins = True
                if not ins:
                    st, end = min(st, newInterval[0]), max(newInterval[1], end)
                    res.append([st, end])
                    ins = True
                else:
                    last = res[-1]
                    if st <= last[1] <= end:
                        last[1] = end
                    elif last[1] < st:
                        res.append(intervals[i])

        if not ins:
            res.append(newInterval)
        return res

print(Solution().insert(intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]))
