class Solution:
    def findLucky(self, arr) -> int:
        best = -1
        for val in set(arr):
            if arr.count(val) == val and val > best:
                best = val
        return best

