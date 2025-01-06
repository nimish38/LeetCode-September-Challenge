import math
class Solution:
    def minEatingSpeed(self, piles, h):

        # remove import as leetcode performance improves
        def canEat(bananas_per_hour):
            cnt = 0
            for pile in piles:
                cnt += math.ceil(pile / bananas_per_hour)
            return cnt <= h

        low, high, best = 1, max(piles), -1
        while low <= high:
            mid = low + (high - low)//2
            if canEat(mid):
                best = mid
                high = mid - 1
            else:
                low = mid + 1
        return best

print(Solution().minEatingSpeed(piles = [30,11,23,4,20], h = 6))