import math
class Solution:
    def successfulPairs(self, spells, potions, success):
        def minLargest(key):
            mid = n // 2
            while key > potions[mid]:
                mid = (n - mid)//2 + mid

            while mid > 0 and key <= potions[mid - 1]:
                mid -= 1

            return n - mid

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