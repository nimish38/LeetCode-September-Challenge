import bisect
class Solution:
    def successfulPairs(self, spells, potions, success: int):
        res = []
        potions = sorted(potions)
        l = len(potions)
        for spell in spells:
            res.append(l - bisect.bisect_left(potions, success/spell))
        return res
print(Solution().successfulPairs(spells = [5,1,3], potions = [1,2,3,4,5], success = 7))