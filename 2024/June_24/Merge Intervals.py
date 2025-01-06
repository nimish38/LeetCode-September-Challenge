class Solution:
    def merge(self, intervals):
        intervals.sort()
        res = []
        for currInterval in intervals:
            if not res or res[-1][1] < currInterval[0]:
                res.append(currInterval)
            else:
                res[-1][1] = max(res[-1][1], currInterval[1])
        return res

print(Solution().merge(intervals = [[2,3],[4,5],[6,7],[8,9],[1,10]]))