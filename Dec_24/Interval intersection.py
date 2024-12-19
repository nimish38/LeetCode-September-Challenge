class Solution:
    def intervalIntersection(self, firstList, secondList):
        res, i, j = [], 0, 0

        while i < len(firstList) and j < len(secondList):
            fs, fe = firstList[i]
            ss, se = secondList[j]
            start, end = max(fs, ss), min(fe, se)
            if start <= end:
                res.append([start, end])
            if fe < se:
                i += 1
            else:
                j += 1
        return res


print(Solution().intervalIntersection(firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]))

