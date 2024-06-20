class Solution:
    def insert(self, intervals, newInterval):
        if not intervals:
            return [newInterval]
        res, start, end, flag = [], newInterval[0], newInterval[1], False
        for int in intervals:
            if not flag:
                if int[0] <= start <= int[1]:
                    res.append([int[0], max(int[1], end)])
                    flag = True
                else:
                    res.append(int)
            else:
                if int[0] <= end <= int[1]:
                    res[-1][1] = int[1]
                elif end < int[0]:
                    res.append(int)
        if not flag:
            res.append(newInterval)
        return res

print(Solution().insert(intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]))

