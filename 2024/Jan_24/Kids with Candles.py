class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        highest = max(candies)
        res =[]
        for num in candies:
            if num + extraCandies >= highest:
                res.append(True)
            else:
                res.append(False)
        return res


val = Solution()
print(val.kidsWithCandies([2,3,5,1,3], 3))