class Solution:
    def insert(self, intervals, newInterval):
        res, start, end, flag = [], newInterval[0], newInterval[1], False
        for int in intervals:
            if not flag:
                if int[0] <= start <= int[1]:
                    res.append(int[0], int[1])
                    flag = True
                else:
                    res.append(int)
            else:
                if int[0] <= end <= int[1]:
                    res[-1][1] = int[1]
                elif end < int[0]:
                    res.append(int)
        return res


