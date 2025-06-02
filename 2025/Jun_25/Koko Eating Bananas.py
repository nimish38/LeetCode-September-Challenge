import math


class Solution(object):
    def minEatingSpeed(self, piles, h):
        start = sum(piles) // h
        l, r = start if start > 0 else 1, max(piles)

        def hourstoeat(val):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / val)
            return hours

        while l < r:
            mid = l + ((r - l) // 2)
            if hourstoeat(mid) <= h:
                r = mid
            else:
                l = mid + 1
        return l

print(Solution().minEatingSpeed(piles = [3,6,7,11], h = 8))