class Solution:
    def candy(self, ratings):
        n = len(ratings)
        candies = n

        i = 1;
        while i < n:
            if ratings[i] == ratings[i - 1]:
                i += 1
                continue

            # // increasing slope
            peak = 0
            while ratings[i] > ratings[i - 1]:
                peak += 1
                candies += peak
                i += 1
                if i == n:
                    return candies

            # // decreasing slope
            dip = 0
            while i < n and ratings[i] < ratings[i - 1]:
                dip += 1
                candies += dip
                i += 1

            candies -= min(peak, dip)
        return candies

print(Solution().candy(ratings = [1,3,4,5,2]))