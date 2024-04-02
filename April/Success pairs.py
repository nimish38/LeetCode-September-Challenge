import math
class Solution:
    def successfulPairs(self, spells, potions, success):
        def minLargest(key):
            low, high, best = 0, n - 1, n
            while low <= high:
                mid = ((high - low) // 2) + low
                if potions[mid] >= key:
                    best = mid
                    high = mid - 1
                else:
                    low = mid + 1
            return n - best

        potions.sort()
        pairs, n = [], len(potions)
        for spell in spells:
            mid = math.ceil(success / spell)
            if mid < potions[0]:
                pairs.append(n)
            elif mid > potions[-1]:
                pairs.append(0)
            else:
                pairs.append(minLargest(mid))
        return pairs

print(Solution().successfulPairs(spells = [5,1,3], potions = [1,2,3,4,5], success = 7))